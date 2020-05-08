# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import User
from .serializers import UserSerializer

class UserView(ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserRUDView(RetrieveUpdateDestroyAPIView):
	lookup_field = 'userId'
	queryset = User.objects.all()
	serializer_class = UserSerializer