from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework import generics, viewsets
from .models import Women
from .serializers import WomenSerializer
from rest_framework.views import APIView, Response
# Create your views here.

class WomenViewSet(viewsets.ModelViewSet):
     queryset = Women.objects.all()
     serializer_class = WomenSerializer
# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

