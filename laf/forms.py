from django.core import validators
from django import forms
from .models import User, Founder

class ItemRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ItemFound(forms.ModelForm):
    class Meta:
        model = Founder
        fields = '__all__'



