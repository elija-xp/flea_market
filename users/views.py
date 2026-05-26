from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View

from users.forms import RegisterForm
from users.services.user_service import UserService
from django.contrib.auth import get_user_model, logout

User = get_user_model()


class UserDetailView(generic.DetailView):
    model = User
    queryset = User.objects.prefetch_related(
        "items__category", "wishlist__category", "purchases__item"
    )


class UserRegisterView(generic.FormView):
    form_class = RegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
    user_service = UserService()

    def form_valid(self, form: RegisterForm):
        url = self.request.build_absolute_uri("/")
        self.user_service.register_user(
            validated_data=form.cleaned_data,
            url=url,
        )
        messages.success(
            self.request, "Check your email to activate your account."
        )
        return super().form_valid(form)


class UserActivateView(View):
    user_service = UserService()

    def get(self, request, uid, token):
        try:
            self.user_service.activate_user(uid=uid, token=token)
            messages.success(request, "Account activated! You can now login.")
        except Exception:
            messages.error(request, "Activation link is invalid or expired.")
        return HttpResponseRedirect(reverse_lazy("login"))


def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')
