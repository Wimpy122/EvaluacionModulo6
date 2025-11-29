from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('tareas/', views.lista_tareas, name='lista_tareas'),
    path('tareas/nueva/', views.agregar_tarea, name='agregar_tarea'),
    path('tareas/<int:tarea_id>/', views.detalle_tarea, name='detalle_tarea'),
    path('tareas/<int:tarea_id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
]