from django import forms
from .models import Product, ProductFeatures, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model= Product 
        fields=[
            'title',
            'quantity',
            'price',
            'description',
            'category',
        ]
        
        
class ImageForm(forms.Form):
    image = forms.ImageField()
    class Meta:
        model = ProductImage
        fields = [
            'image',
        ]
        
class FeatureForm(forms.ModelForm):
    class Meta:
        model = ProductFeatures
        fields = [
            'label',
            'value',
        ]
        
