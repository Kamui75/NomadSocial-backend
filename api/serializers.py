
from rest_framework import serializers
from .models import Useraccount


class UseraccountSerialize(serializers.ModelSerializer):
    class Meta:
        model = Useraccount
        fields = ['prenom', 'nom', 'email', 'password']
