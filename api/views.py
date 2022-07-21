from django.shortcuts import render
from .serializers import UseraccountSerialize
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Useraccount
from rest_framework.response import Response

class ListUser(generics.ListAPIView):
    queryset = Useraccount.objects.all()
    serializer_class = UseraccountSerialize

class CreateUser(generics.CreateAPIView):
    queryset = Useraccount.objects.all()
    serializer_class = UseraccountSerialize

    