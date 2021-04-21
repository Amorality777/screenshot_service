from django.contrib import admin

# Register your models here.
from .models import Task, Screenshot

admin.register(Task)
admin.register(Screenshot)
