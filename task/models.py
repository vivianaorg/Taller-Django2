from django.db import models
from django.utils import timezone
from datetime import datetime

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField("Fecha de vencimiento")
    completed = models.BooleanField(default=False)

    # Metodo que regresa el nombre de la tarea
    def __str__(self):
        return self.name
    
    # Metodo que compara la fecha de vencimiento de la tarea con la fecha y hora actuales, retorna true si es menor
    def is_past_due(self):
        return self.due_date < timezone.now()