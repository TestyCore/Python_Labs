from django import forms
from edostavka.models import Product, ProductCategory


class ProductForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=ProductCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Product
        fields = ('title', 'category', 'price', 'composition', 'ean', 'manufacturer')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['category'].initial = self.instance.category.all()

    def save(self, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save()
        if self.cleaned_data['category']:
            product.category.set(self.cleaned_data['category'])
        else:
            product.category.clear()
        self.save_m2m()
        return product
