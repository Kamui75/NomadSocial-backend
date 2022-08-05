from asyncio import mixins
from django.shortcuts import render
from .serializers import CompanyAccountSerialize, UserAccountSerialize
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import CompanyAccount, UserAccount
from rest_framework.response import Response
from rest_framework import mixins

class ListUser(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerialize

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
         

class CreateUser(mixins.CreateModelMixin, generics.GenericAPIView ):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerialize

    def post(self, request, *args, **kwargs):
       return self.create(request, *args, **kwargs)

class CreateCompanyAccount(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = CompanyAccount.objects.all()
    serializer_class = CompanyAccountSerialize
    
    def post(self, request, *args, **kwargs):
       return self.create(request, *args, **kwargs)
    
class ListCompanyAccount(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = CompanyAccount.objects.all()
    serializer_class = CompanyAccountSerialize

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)