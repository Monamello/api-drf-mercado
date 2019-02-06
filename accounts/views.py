from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer
from compra.serializer import CompraSerializer

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserCompraViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(compras__isnull=False).distinct()
    serializer_class = UserSerializer
