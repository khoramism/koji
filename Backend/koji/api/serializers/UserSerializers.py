from account.models import UserProfile
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['email', 'name', 'is_active', 'is_staff']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['email', 'name',"password"]
    
    def create(self, validated_data):
        user = UserProfile(
            email=validated_data["email"],
            name=validated_data["name"],
            is_active=True
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
