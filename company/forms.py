from django import forms
from django.forms import ModelForm
from landingpage.models import Company

class LengkapiFormCompany(ModelForm):
    class Meta:
        model = Company
        fields = ('name_company', 'email', 'logo_image', 'bidang_usaha', 'alamat', 'link_linkedin', 'link_instagram')
