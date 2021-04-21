from rest_framework import generics, status
from rest_framework.response import Response

from service.tasks import create_task


class CreateTaskAPI(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):
        url, depth = request.query_params.get('url'), request.query_params.get('depth'),
        create_task(url, depth)
        data = {'task': 'id'}
        headers = self.get_success_headers(data)
        return Response(data=data, status=status.HTTP_200_OK, headers=headers)
