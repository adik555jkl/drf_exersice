from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'opisanie', 'data', 'stat']
        read_only_fields = ['id', 'data']
