from django.shortcuts import render

from rest_framework import viewsets 

from .models import Lead 
from .serializers import LeadSerializer  

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import(
	BasicAuthentication,
	SessionAuthentication,
	TokenAuthentication
)

class LeadViewSet(viewsets.ModelViewSet):
	#authentication_classes = [BasicAuthentication]
	#authentication_classes = [TokenAuthentication]
	#authentication_classes = [SessionAuthentication]
	#permission_classes = [IsAuthenticated]
	queryset = Lead.objects.all()
	serializer_class = LeadSerializer


