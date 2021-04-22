from django.db import models
from django_celery_results.models import TaskResult


class Screenshot(models.Model):
    task = models.ForeignKey(TaskResult, related_name='screenshots', on_delete=models.SET_NULL, null=True)
    image = models.ImageField()
