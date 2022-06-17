from django.forms import ModelForm, TextInput
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={"type": "text", "maxlength": "50"}),
            'description': TextInput(attrs={"type": "text", "maxlength": "400"}),
            'price': TextInput(attrs={"type": "number", "min": "1", "max": "10000"})
        }
