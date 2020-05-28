from django import forms
from django.forms import ModelForm
from .models import BugTracker

class TicketForm(ModelForm):
    class Meta:
        model = BugTracker
        fields = ['title', 'description', 'ticket_status']
        # labels = {
        #     'ticket_type': _('Ticket Type'),
        # }
        help_texts = {
            'ticket_type': _('Please note: Feature request priority')
        }