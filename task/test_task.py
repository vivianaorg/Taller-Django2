import pytest  # type: ignore
from django.urls import reverse
from django.test import Client
from task.models import Task
from django.core.serializers import serialize
import json


@pytest.mark.django_db
def test_index_view():
    client = Client()
    response = client.get(reverse("task:index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_tareasvencidas():
    client = Client()
    all_tasks = Task.objects.all()
    tasks_json = json.loads(serialize("json", all_tasks))
    for task_json in tasks_json:
        task_dict = task_json["fields"]
        response = client.get(reverse("task:detail", args=(task_dict["id"],)))
        assert response.status_code == 200
        assert not task_dict["is_past_due"]


@pytest.mark.django_db
def test_completed():
    client = Client()
    all_tasks = Task.objects.all()
    for task in all_tasks:
        response = client.get(reverse("task:detail", args=(task.id,)))
        assert response.status_code == 200
        assert task.completed
        assert "Completado" in response.content.decode()


@pytest.mark.django_db
def test_nombre_vacio():
    all_tasks = Task.objects.all()
    for task in all_tasks:
        assert task.name != ""
