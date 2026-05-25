from django import forms

from django.contrib.auth.forms import UserCreationForm

from market.models import Item, User


class ItemSearchForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title..."}),
    )


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["title", "description", "price", "category"]


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name")
