from django.shortcuts import render
from .models import Task
from datetime import date
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def tasks(request):
    if request.method == 'GET':
     tasks = Task.objects.all()
     serializer = TaskSerializer(tasks, many = True)
     return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save();
    return Response(serializer.data, status= status.HTTP_201_CREATED)
@api_view(['GET', 'PUT', 'DELETE'])
def taskdetails(request, pk):
    try:
        task = Task.objects.get(pk = pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status= status.HTTP_200_OK)
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)