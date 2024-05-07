from django.http import HttpResponse
#Devuelve una respuesta HTTP básica
from django.http import Http404
from django.shortcuts import render
from .models import Task
from django.http import JsonResponse
import json

def index(request):
    latest_task_list = Task.objects.order_by("-due_date")[:5]
    context = {
        "latest_task_list": latest_task_list,
    }
    return render(request,"task/index.html",context)

def detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("La tarea solicitada no existe")
    return render(request, "task/detail.html", {"task": task})

def tareaJson(request):
    tareas_data = list(Task.objects.values())
    return JsonResponse(tareas_data, safe=False)