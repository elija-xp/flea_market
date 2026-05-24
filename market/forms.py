from django import forms

from market.models import Item


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
