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
        fields = ("name", "bio")

    def create(self, validated_data):
        creatorUser = self.context["request"].user
        teamUsers = self.context["request"].data.get("users")
        if not teamUsers:
            teamUsers = [creatorUser.pk]
        elif creatorUser.pk not in teamUsers:
            teamUsers.append(creatorUser.pk)

        team = Team(
            creator=creatorUser,
            name=validated_data["name"],
            bio=validated_data["bio"]
        )
        team.save()
        team.users.set(teamUsers)
        team.save()
        return team


class TeamEventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"
