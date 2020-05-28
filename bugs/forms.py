from django import forms

# from django.forms import ModelForm
from .models import BugTracker


class TicketForm(forms.Form):
    title = forms.CharField(max_length=100)
    details = forms.CharField(widget=forms.Textarea)
