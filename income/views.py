# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import RetrieveAPIView

from .models import Income
from .serializers import IncomeSerializer

class IncomeView(ListCreateAPIView):
	queryset = Income.objects.all()
	serializer_class = IncomeSerializer

class IncomeRUDView(RetrieveUpdateDestroyAPIView):
	lookup_field = 'incomeId'
	queryset = Income.objects.all()
	serializer_class = IncomeSerializer

class IncomesRView(RetrieveAPIView):
	lookup_field = 'user'
	queryset = Income.objects.all()
	serializer_class = IncomeSerializer