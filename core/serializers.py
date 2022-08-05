from rest_framework import serializers
from .models import CompanyAccount, UserAccount


class UserAccountSerialize(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id','firstname', 'name', 'email', 'password']


class CompanyAccountSerialize(serializers.ModelSerializer):
    class Meta:
        model = CompanyAccount
        fields = ['id','company_name', 'contact_email', 'password']