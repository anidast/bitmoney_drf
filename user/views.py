# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
	HTTP_203_NON_AUTHORITATIVE_INFORMATION,
	HTTP_201_CREATED,
	HTTP_202_ACCEPTED,
)

from .models import User
from .serializers import UserSerializer

class UserView(ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserRUDView(RetrieveUpdateDestroyAPIView):
	lookup_field = 'userId'
	queryset = User.objects.all()
	serializer_class = UserSerializer

class LoginView(APIView):
	def post(self, request):
		context = {}
		email = request.data.get('email')
		password = request.data.get('password')
		UserModel = get_user_model()
		users = None
		try:
			user = UserModel.objects.get(email=email)
		except UserModel.DoesNotExist:
			users = None
		else:
			if user.check_password(password):
				users = user
		if users:
			# token, created = Token.objects.get_or_create(user=users)
			context['status'] = 1
			context['response'] = 'Success'
			# context['token'] = token.key
			context['userId'] = users.userId
		else:
			context['status'] = 0
			context['response'] = 'Error'
			context['message'] = 'Invalid email or password'
			return Response(context,status=HTTP_203_NON_AUTHORITATIVE_INFORMATION)

		return Response(context,status=HTTP_202_ACCEPTED)