from rest_framework import status, viewsets
from rest_framework.response import Response
from celery.result import AsyncResult
from service.permissions import CheckParams, CheckTaskId
from service.tasks import parse


class CreateTaskAPI(viewsets.ViewSet):
    def get_permissions(self):
        permissions = []
        if self.action == 'create':
            permissions.append(CheckParams())
        elif self.action == 'retrieve':
            permissions.append(CheckTaskId())
        return permissions

    def create(self, request):
        url, depth = request.query_params.get('url'), request.query_params.get('depth'),
        task = parse.delay(url, depth)
        data = {'task': task.id}
        return Response(data=data, status=status.HTTP_200_OK)

    def retrieve(self, request):
        task_id = request.query_params.get('task_id')
        res = AsyncResult(task_id)
        data = {
            'status': res.status
        }
        return Response(data=data, status=status.HTTP_200_OK)
