from rest_framework import serializers
from .models import Screenshot
from django_celery_results.models import TaskResult


class ScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screenshot
        fields = ('id', 'image')


class TaskSerializer(serializers.ModelSerializer):
    screenshots = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = TaskResult
        fields = ('id', 'task_id', 'task_name', 'status', 'screenshots')


class TaskInProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResult
        fields = ('id', 'task_id', 'task_name', 'status')
