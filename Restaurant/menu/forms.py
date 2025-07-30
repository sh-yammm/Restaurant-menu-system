from django import forms
from .models import MenuItem

class MenuItemForm(forms.ModelForm):

    class Meta:

        model = MenuItem
        exclude = ['created_at', 'updated_at'] 

        widgets = {

            'menu': forms.Select(attrs={'class': 'form-control'}),

            'name': forms.TextInput(attrs={'class': 'form-control'}),

            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),

            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),

        }
        # fields = ['menu', 'name', 'description', 'price']

# Form for updating price and vegetarian status
class UpdatePriceForm(forms.ModelForm):

    class Meta:
        model = MenuItem
        
        fields = ["price", "is_vegetarian"]