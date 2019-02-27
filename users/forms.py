from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    student_email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'student_email', 'password1', 'password2', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        #user.first_name = cleaned_data['first_name']
        #user.last_name = cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user = user.save()
            UserProfile.objects.create(user=user, student_email=self.cleaned_data['student_email'])



        return user

    def clean_student_email(self): 
        email = self.cleaned_data['student_email']
        if 'umk' not in email:
            raise forms.ValidationError("Zły email podaj swój email uczennianny")
        return email


class EditProfileForm(UserChangeForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'image']


    def save(self, commit=True):
        user = super(EditProfileForm, self).save(commit=False)
        #user.first_name = cleaned_data['first_name']
        #user.last_name = cleaned_data['last_name']
        #user.email = cleaned_data['email']
        user.userprofile.image = self.cleaned_data['image']

        if commit:
            user.save()

        return user