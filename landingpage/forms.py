from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, Textarea
from landingpage.models import *
from django import forms


class EOForm(forms.ModelForm):    
    class Meta:
        model = user_EO
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
        model = user_company
        fields = ('user', 'name_company', 'email')
        exclude = ['user']