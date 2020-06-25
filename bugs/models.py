from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


class BugTracker(models.Model):
    """Trouble tickets"""

    title = models.TextField(max_length=50)
    time_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1000)
    bug_reporter = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="bug_reporter",
        null=True,
        default=None,
    )
    assign_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="assign_user",
        null=True,
        default=None,
    )
    completed_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="completed_by",
        null=True,
        default=None,
    )

    NEW = "New"
    IN_PROGRESS = "In Progress"
    DONE = "Done"
    INVALID = "Invalid"

    TICKET_STATUS_CHOICES = [
        (NEW, "New"),
        (IN_PROGRESS, "In Progress"),
        (DONE, "Done"),
        (INVALID, "Invalid"),
    ]
    ticket_status = models.CharField(
        max_length=25, choices=TICKET_STATUS_CHOICES, default=NEW
    )

    def __str__(self):
        return self.title
