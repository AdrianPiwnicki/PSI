from django.shortcuts import render
from .models import Klient
from .serializers import KlientSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

def questions_list1(request):
    if request.method == 'GET':
        questions = Klient.objects.all()
        serializer = KlientSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        dane = JSONParser().parse(request)
        serializer = KlientSerializer(data=dane)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
#-----------------------------------------------------------------
@api_view(['GET','POST'])
def question_list(request, format=None):
    if request.method=='GET':
        questions = Klient.objects.all()
        serializer = KlientSerializer(questions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = KlientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
