from django.urls import path

from . import views

#Define un espacio de nombres para las URL de la aplicación task
app_name="task"

#contiene las rutas de URL para la aplicación.
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:task_id>/", views.detail, name="detail"),
]