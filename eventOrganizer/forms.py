from django import forms
from django.forms import ModelForm
from landingpage.models import Event

class LengkapiForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name_event', 'email', 'logo_image', 'alamat', 'link_linkedin', 'link_instagram')
