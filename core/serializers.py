from rest_framework import serializers
from .models import  UserAccount


class UserAccountSerialize(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id','first_name', 'last_name', 'email', 'password','password2']


class CompanyAccountSerialize(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id','first_name','last_name','company_name', 'email', 'password', 'password2']