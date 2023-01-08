from django import forms

class MessageForm(forms.Form):
    recipient = forms.CharField(max_length=255)
    chat = forms.CharField(widget=forms.Textarea)
