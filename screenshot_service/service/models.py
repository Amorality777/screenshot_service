from django.db import models


class Task(models.Model):
    task_id = models.CharField(max_length=50)
    url = models.URLField()
    depth = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.url} {self.depth}'


class Screenshot(models.Model):
    task = models.ForeignKey('Task', related_name='screenshots', on_delete=models.SET_NULL, null=True)
    image = models.ImageField()
