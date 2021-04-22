from django.urls import path

from .views import CreateTaskAPI

urlpatterns = [
    path('screenshot/', CreateTaskAPI.as_view({'post': 'create'}), name='screenshot'),
    path('screenshot/<int:pk>', CreateTaskAPI.as_view({'get': 'screenshot'}), name='screenshot'),
    path('check/<int:pk>', CreateTaskAPI.as_view({'get': 'retrieve'}), name='check'),
]
