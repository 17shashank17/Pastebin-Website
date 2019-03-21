from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from share.models import RichText
from django.db import models
from django.forms import ModelForm

class SignupForm(UserCreationForm):

    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
        def save(self,commit=True):
            user=super(SignupForm,self).save(commit=False)
            user.first_name=cleaned_data('first_name')
            user.last_name=cleaned_data('last_name')
            user.email=cleaned_data('email')

            if commit:
                user.save()

class Rich(forms.ModelForm):
    class Meta:
        model=RichText
        fields=(
            'content_images',
        )