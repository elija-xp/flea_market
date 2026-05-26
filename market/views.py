from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model

from market.forms import ItemSearchForm, ItemForm
from market.models import Item, Category, Deal

User = get_user_model()


def index(request: HttpRequest) -> HttpResponse:
    num_items = Item.objects.count()
    num_users = User.objects.count()
    num_categories = Category.objects.count()
    num_deals = Deal.objects.count()
    recent_items = Item.objects.select_related("category", "seller")
    context = {
        "num_items": num_items,
        "num_users": num_users,
        "num_categories": num_categories,
        "num_deals": num_deals,
        "recent_items": recent_items,
    }
    return render(request, "market/index.html", context)


class ItemListView(generic.ListView):
    model = Item
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = ItemSearchForm(initial={"title": title})
        context["categories"] = Category.objects.all()
        context["selected_category"] = self.request.GET.get("category", "")
        return context

    def get_queryset(self):
        queryset = Item.objects.select_related("category", "seller")
        form = ItemSearchForm(self.request.GET)
        if form.is_valid() and form.cleaned_data.get("title"):
            queryset = queryset.filter(
                title__icontains=form.cleaned_data["title"]
            )
        category_id = self.request.GET.get("category")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class ItemDetailView(generic.DetailView):
    model = Item
    pass


class ItemCreateView(generic.CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy("market:item-list")

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)
    pass


class ItemUpdateView(generic.UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy("market:item-list")

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)
    pass


class ItemDeleteView(generic.DeleteView):
    model = Item
    success_url = reverse_lazy("market:item-list")
    pass


def buy_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if not hasattr(item, "deal") and item.seller != request.user:
        Deal.objects.create(item=item, buyer=request.user)
    return HttpResponseRedirect(
        reverse_lazy("market:item-detail", args=[pk])
    )


def toggle_wishlist(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item in request.user.wishlist.all():
        item.wished_by.remove(request.user)
    else:
        item.wished_by.add(request.user)
    return HttpResponseRedirect(reverse_lazy("market:item-detail", args=[pk]))
