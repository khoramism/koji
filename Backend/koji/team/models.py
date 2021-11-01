from django.db import models
import uuid
# Create your models here.


class Team(models.Model):
    creator = models.ForeignKey(
        'account.UserProfile', on_delete=models.CASCADE, related_name='creator_team')

    name = models.CharField(max_length=50)

    users = models.ManyToManyField('account.UserProfile')

    invite_id = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=True)

    bio = models.TextField()

    def __str__(self) -> str:
        return self.name
