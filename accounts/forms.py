from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()


class CustomUserCreationForm(UserCreationForm):  
   
   class Meta:
        
        model = get_user_model()
        fields = [
            "username", 
            "first_name",
            "last_name",
            "email",
        ]

        labels = {
            "username": "아이디",
            "first_name": "성함",
            "last_name": "닉네임",
            "email": "email",
        }

class CustomAuthenticationForm(AuthenticationForm):

    username = forms.CharField(
        label=_("아이디"),
        widget=forms.TextInput(attrs={"autofocus": True}),
    )

class CustomUserChangeForm(UserChangeForm):
    pass