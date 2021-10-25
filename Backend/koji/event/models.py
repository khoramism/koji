from django.db import models
#from koji.Backend.koji.account.models import UserProfile
#from koji.Backend.koji.team.models import Team
import uuid
# Create your models here.
class Event(models.Model):
    STATUS = (
        ('expired','گذشته شده'),
        ('indecisive','فرا نرسیده'),
        ('voting', 'در حال رای گیری')
    )

    title = models.CharField(max_length=50)
    
    description = models.TextField()

    status = models.CharField(choices=STATUS, max_length=50)

    creator = models.ForeignKey("account.UserProfile", on_delete=models.CASCADE, related_name='event_creator')

    users = models.ManyToManyField("account.UserProfile")

    teams = models.ManyToManyField("team.Team")
    
    invite_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
