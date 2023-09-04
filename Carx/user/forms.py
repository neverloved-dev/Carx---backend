from django import forms
from .models import OrdinaryUser

class UserRegistrationForm(forms.Form):
    email = forms.EmailField( max_length=100, required = True)
    first_name = forms.CharField( max_length=100,required = True)
    last_name = forms.CharField( max_length=100, required = True)
    phone_number=forms.CharField(max_length=200, required = True)

    class Meta:
        model = OrdinaryUser
        fields = ['email', 'first_name', 'last_name', 'phone+number']