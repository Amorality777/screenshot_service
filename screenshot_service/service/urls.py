from django.urls import path

from .views import CreateTaskAPI

urlpatterns = [
    path('task/', CreateTaskAPI.as_view({'post': 'create', 'get': 'retrieve'}), name='create-task'),
]
