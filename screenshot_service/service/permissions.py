from rest_framework.permissions import BasePermission


class CheckParams(BasePermission):
    message = "required parameter 'url'/'depth' is not specified"

    def has_permission(self, request, view):
        url = request.query_params.get('url')
        depth = request.query_params.get('depth')
        return url and depth


class CheckTaskId(BasePermission):
    message = "required parameter 'task_id' is not specified"

    def has_permission(self, request, view):
        return request.query_params.get('task_id')
