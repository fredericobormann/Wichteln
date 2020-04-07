from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import Party, Donation
from .serializers import UserSerializer


# Create your views here.
class UserList(generics.ListAPIView):
    """ View to list all users"""
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)