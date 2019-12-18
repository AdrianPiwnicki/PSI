from .models import Klient, Wypożyczanie, Pracownik, Samochód
from .serializers import KlientSerializer, WypozyczanieSerializer, SamochodSerializer, PracownikSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions

class KlientList(APIView):
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]

   def get(self, request, format=None):
       questions = Klient.objects.all()
       serializer = KlientSerializer(questions, many=True)
       return Response(serializer.data)

   def post(self, request, format=None):
       serializer = KlientSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save(owner=self.request.user)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KlientDetail(APIView):
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]

   def get_object(self, pk):
       try:
           return Klient.objects.get(pk=pk)
       except Klient.DoesNotExist:
           raise Http404

   def get(self, request, pk, format=None):
       question = self.get_object(pk)
       serializer = KlientSerializer(question)
       return Response(serializer.data)

   def put(self, request, pk, format=None):
       question = self.get_object(pk)
       serializer = KlientSerializer(question, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   def delete(self, request, pk, format=None):
       question = self.get_object(pk)
       question.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)


# class UserList(generics.ListAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
