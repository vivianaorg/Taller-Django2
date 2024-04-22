from django.http import HttpResponse
#Devuelve una respuesta HTTP básica
from django.http import Http404
from django.shortcuts import render
from .models import Task

def index(request):
    #Ordena las tareas por fecha de vencimiento y muestra las primeras 5 tareas
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