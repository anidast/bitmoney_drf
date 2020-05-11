# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListAPIView

from .models import Outcome
from .serializers import OutcomeSerializer

class OutcomeView(ListCreateAPIView):
	queryset = Outcome.objects.all()
	serializer_class = OutcomeSerializer

class OutcomeRUDView(RetrieveUpdateDestroyAPIView):
	lookup_field = 'outcomeId'
	queryset = Outcome.objects.all()
	serializer_class = OutcomeSerializer

class OutcomesRView(ListAPIView):
	lookup_field = 'user'
	queryset = Outcome.objects.all()
	serializer_class = OutcomeSerializer