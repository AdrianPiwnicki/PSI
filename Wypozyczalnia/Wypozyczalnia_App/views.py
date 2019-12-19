# from Wypozyczalnia_App.models import *
# from Wypozyczalnia_App.models import *
from .models import *
from .serializers import *
from rest_framework import generics, status
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from rest_framework import permissions




class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer


class KlientDetail(generics.RetrieveDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer


class SamochodList(generics.ListCreateAPIView):
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer


class SamochodDetail(generics.RetrieveDestroyAPIView):
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer


class PracownikList(generics.ListCreateAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer


class PracownikDetail(generics.RetrieveDestroyAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer


class WypozyczanieList(generics.ListCreateAPIView):
    queryset = Wypozyczanie.objects.all()
    serializer_class = WypozyczanieSerializer


class WypozyczanieDetail(generics.RetrieveDestroyAPIView):
    queryset = Wypozyczanie.objects.all()
    serializer_class = WypozyczanieSerializer