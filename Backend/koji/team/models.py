from django.db import models
#from koji.Backend.koji.account.models import UserProfile
#from koji.Backend.koji.event.models import Event

# Create your models here.
class Team(models.Model):
    creator = models.ForeignKey('account.UserProfile', on_delete= models.CASCADE, related_name='creator_team')

    name = models.CharField(max_length=50)

    users = models.ManyToManyField('account.UserProfile')

    bio = models.TextField()

    def __str__(self) -> str:
        return self.name