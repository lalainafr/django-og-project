from .models import Product
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
        
        widgets = {
          'Description': forms.Textarea(attrs={'rows':4}),
        }
        
