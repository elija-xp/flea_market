from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth import login

from users.forms import RegisterForm
from users.services.user_service import UserService
from django.contrib.auth import get_user_model, logout

User = get_user_model()


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    queryset = User.objects.prefetch_related(
        "items__category", "wishlist__category", "purchases__item"
    )


class UserRegisterView(generic.FormView):
    form_class = RegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("market:index")
    user_service = UserService()

    def form_valid(self, form: RegisterForm):
        try:
            user = self.user_service.register_user(
                validated_data=form.cleaned_data,
                url=None
            )
        except Exception:
            form.add_error(
                None, "There was an error creating your account."
                      " This email already exist."
            )
            return self.form_invalid(form)

        login(self.request, user)
        messages.success(self.request, "Account created!")
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, "registration/logged_out.html")
