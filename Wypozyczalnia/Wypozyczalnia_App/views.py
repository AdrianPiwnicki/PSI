from Wypozyczalnia_App.models import *
from Wypozyczalnia_App.serializers import *
from rest_framework import generics
from rest_framework import permissions


class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer


class KlientDetail(generics.RetrieveDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer

# Create your views here.
