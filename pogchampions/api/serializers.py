from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ("id", "discord_id", "email", "user_tag", "created_at")