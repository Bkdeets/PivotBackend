from django.shortcuts import render
from .serializers import UserSerializer
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework import exceptions, generics

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)


class StrategyViewSet(viewsets.ModelViewSet):
    serializer_class = StrategySerializer
    queryset = Strategy.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
