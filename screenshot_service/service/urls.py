from django.urls import path

from .views import CreateTaskAPI

urlpatterns = [
    path('create-task/', CreateTaskAPI.as_view(), name='create-task'),
]
