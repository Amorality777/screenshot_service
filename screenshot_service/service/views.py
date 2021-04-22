from time import sleep

from django.http import Http404
from django_celery_results.models import TaskResult
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from service.models import Screenshot
from service.serializers import TaskSerializer, TaskInProcessSerializer, ScreenshotSerializer
from service.tasks import parse


class CreateTaskAPI(viewsets.ModelViewSet):
    queryset = TaskResult

    def create(self, request, *args, **kwargs):
        url, depth = request.query_params.get('url'), request.query_params.get('depth'),
        task = parse.delay(url, depth)
        """Задержка для инициализации экземпляра модели"""
        sleep(1)
        task = TaskResult.objects.get(task_id=task.id)
        serializer = TaskInProcessSerializer(instance=task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        obj = self.get_object()
        if obj.status == 'SUCCESS':
            return TaskSerializer
        return TaskInProcessSerializer

    @action(detail=True, methods=['get'])
    def screenshot(self, request, pk):
        instance = Screenshot.objects.filter(pk=pk).first()
        if not instance:
            raise Http404
        serializer = ScreenshotSerializer(instance)
        return Response(serializer.data)
