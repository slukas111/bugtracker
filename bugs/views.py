from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import BugTracker
from django.contrib.auth import logout, login, authenticate
from django.utils import timezone
from bugs.models import CustomUser, AbstractUser
from django.views.generic.edit import FormView
from django.views.generic import View
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, TicketForm, EditTicketForm
from django.contrib.auth.decorators import login_required

# this works
@login_required
def index(request):
    html = "index.html"
    ticket_data = BugTracker.objects.all()
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BugTracker.objects.create(
                ticket_status="New",
                title=data["title"],
                description=data["description"],
                bug_reporter=request.user,
            )
            return HttpResponseRedirect(reverse("homepage"))

    return render(request, "index.html", {"form": form, "ticket_data": ticket_data})

# this works
class LoginView(View):
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/login/")

        return render(request, "/")

    def get(self, request):
        return render(request, "login.html", {"form": CustomUserCreationForm()})

# this works
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/login/")


# Sign Up View this works
class SignUpView(FormView):
    template_name = "signup.html"
    success_url = reverse_lazy("login")

    def get(self, request):
        return render(request, self.template_name, {"form": CustomUserCreationForm()})

    def post(self, request):
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = CustomUser.objects.create_user(
                    username=data["username"], password=data["password"]
                )
                login(request, user)
                return HttpResponseRedirect("/login/")

            else:
                for msg in form.error_messages:
                    print(form.error_messages[msg])

                return render(
                    request=request,
                    template_name="signup.html",
                    context={"form": form},
                )

@login_required
def edit_ticket(request, id):
    ticket = BugTracker.objects.get(id=id)
    if request.method == "POST":
        form = EditTicketForm(request.POST, instance=ticket)
        form.save()
        return HttpResponseRedirect("/")
    form = EditTicketForm(instance=ticket)
    return render(request, "index.html", {"form": form})

@login_required
def ticket_detail(request, id):
    ticket = BugTracker.objects.get(id=id)
    return render(request, "ticket_detail.html", {"ticket": ticket})

@login_required
def assign_ticket(request, id):
    ticket = BugTracker.objects.get(id=id)
    ticket.ticket_status = "In Progress"
    ticket.assign_user = request.user
    ticket.completed_by = None
    ticket.status = "IN_PROGRESS"
    ticket.save()
    return HttpResponseRedirect(reverse("ticket_detail", args=(id,)))
