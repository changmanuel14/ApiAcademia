from django.urls import path
from .views import SexoView, EstadoView, EstudianteView

urlpatterns =[
    path('sexos/', SexoView.as_view(), name='sexos_list'),
    path('sexos/<int:id>', SexoView.as_view(), name='sexos_process'),
    path('estados/', EstadoView.as_view(), name='estados_list'),
    path('estados/<int:id>', EstadoView.as_view(), name='estados_process'),
    path('estudiantes/', EstudianteView.as_view(), name='estudiantes_list'),
    path('estudiantes/<int:id>', EstudianteView.as_view(), name='estudiantes_process'),
    ]