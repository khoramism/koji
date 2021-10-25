import uuid
from django.db import models



class Event(models.Model):
    STATUS = (
        ('ended', 'برگزار شده'),
        ('pending', 'فرا نرسیده'),
        ('voting', 'در حال رای گیری')
    )

    title = models.CharField(max_length=50)

    description = models.TextField(blank=True)

    status = models.CharField(choices=STATUS, max_length=50)

    creator = models.ForeignKey(
        "account.UserProfile", on_delete=models.CASCADE, related_name='event_creator')

    users = models.ManyToManyField("account.UserProfile",blank=True)

    teams = models.ManyToManyField("team.Team")

    invite_id = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=True)

    created = models.DateTimeField(auto_now_add=True)
