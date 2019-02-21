from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


    def clean_email(self): #TODO Test it if it work
            email = self.cleaned_data['email']
            if 'umk' not in email:
                raise forms.ValidationError("Zły email podaj swój email uczennianny")
            return email
