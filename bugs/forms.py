from django import forms
from .models import BugTracker
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(forms.Form):

    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class TicketForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)


class EditTicketForm(forms.ModelForm):
    class Meta:
        model = BugTracker
        fields = ["title", "description", "assign_user", "ticket_status"]
