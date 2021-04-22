from rest_framework.permissions import BasePermission

from service.utils import check_url


class CheckParams(BasePermission):
    def has_permission(self, request, view):
        url = request.query_params.get('url')
        depth = request.query_params.get('depth')
        return url and check_url(url) and depth and int(depth) < 6


class CheckTaskId(BasePermission):
    def has_permission(self, request, view):
        return request.query_params.get('task_id')
