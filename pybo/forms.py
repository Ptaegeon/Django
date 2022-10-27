from django import forms

from .models import Coffee  # Model 호출

class CoffeeForm(forms.ModelForm):  # ModelForm을 상속받는 Coffee
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice')
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'price' : forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name' : '음료 이름',
            'price' : '가격',
        }
