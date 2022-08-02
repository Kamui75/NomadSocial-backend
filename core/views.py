from django.shortcuts import render
from .serializers import UserAccountSerialize
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import UserAccount
from rest_framework.response import Response

class ListUser(generics.ListAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerialize

class CreateUser(generics.CreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerialize
