from rest_framework import serializers
from .models import UserAccount


class UserAccountSerialize(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['firstname', 'name', 'email', 'password']