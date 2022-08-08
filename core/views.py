from asyncio import mixins
from contextlib import nullcontext
from django.shortcuts import render
from .serializers import CompanyAccountSerialize, UserAccountSerialize
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import UserAccount
from rest_framework.response import Response
from rest_framework import mixins

class UserListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerialize

    def get(self, request, *args, **kwargs):
        
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
         
class UserDetailView(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView ):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerialize

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
                                                        
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)







