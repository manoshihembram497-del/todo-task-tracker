from rest_framework import serializers
from .models import Task
from .import views


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'