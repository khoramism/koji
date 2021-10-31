from event.models import Event
from team.models import Team
from account.models import UserProfile
from rest_framework import serializers


class TeamUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["name", "is_active", "email"]


class TeamSerializer(serializers.ModelSerializer):
    users = TeamUsersSerializer(many=True, read_only=True)
    creator = TeamUsersSerializer(many=False, read_only=True)

    class Meta:
        model = Team
        fields = "__all__"


class TeamCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = "__all__"


class TeamEventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"
