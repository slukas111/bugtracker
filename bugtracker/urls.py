"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from bugs import views
from bugs.models import BugTracker
from bugs.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="homepage"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("edit_ticket/<int:id>", edit_ticket, name="edit_ticket"),
    # path("create_ticket/", views.create_ticket, name="create_ticket"),
    path("ticket_detail/<int:id>", views.ticket_detail, name="ticket_detail"),
    path("assign_ticket/edit/<int:id>", views.assign_ticket, name="assign_ticket"),
]
