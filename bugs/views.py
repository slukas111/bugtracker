from django.shortcuts import render
from .models import BugTracker
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.utils import timezone


# Create your views here.
def index(request):
    html = "index.html"
    new_tickets = BugTracker.objects.filter(ticket_status="New")
    in_progress_tickets = BugTracker.objects.filter(ticket_status="In Progress")
    completed_tickets = BugTracker.objects.filter(ticket_status="Done")
    invalid_tickets = BugTracker.objects.filter(ticket_status="Invalid")
    context = {
        "new_tickets": new_tickets,
        "in_progress_tickets": in_progress_tickets,
        "completed_tickets": completed_tickets,
        "invalid_tickets": invalid_tickets,
    }
    return render(request, html, context)
