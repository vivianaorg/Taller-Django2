from django.contrib import admin

from .models import Task
from.models import Category
admin.site.register(Task)
admin.site.register(Category)