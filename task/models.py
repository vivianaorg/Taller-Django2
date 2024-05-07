from django.db import models
from django.utils import timezone
from datetime import datetime

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField("Fecha de vencimiento")
    completed = models.BooleanField(default=False)
    class Meta:
        app_label = 'task'

    # Metodo que regresa el nombre de la tarea
    def __str__(self):
        return self.name
    
    # Metodo que compara la fecha de vencimiento de la tarea con la fecha y hora actuales, retorna true si es menor
    def is_past_due(self):
        return self.due_date > timezone.now()
    
class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    def _str_(self):
        return self.user_name
    
    class Meta:
        app_label = 'task'
    
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    def _str_(self):
        return self.category_name
    class Meta:
        app_label = 'task'