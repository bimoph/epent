from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, Textarea
from landingpage.models import *
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'is_EO', 'is_company')

class EOForm(forms.ModelForm):    
    class Meta:
        model = Event
        fields = ('user', 'name_event', 'email')
        exclude = ['user']
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Masukkan title',
        #         'required': 'true'
        #         }),
        #     'deskripsi': forms.TextInput(attrs={
        #         'class': "form-control", 
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Masukkan deskripsi'
        #         })
        # }
    

class CompanyForm(forms.ModelForm):    
    class Meta:
        model = Company
        fields = ('user', 'name_company', 'email')
        exclude = ['user']