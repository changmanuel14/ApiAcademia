from django.urls import path
from .views import SexoView, EstadoView, EstudianteView, CatedraticoView, AdministrativoView

urlpatterns =[
    path('sexos/', SexoView.as_view(), name='sexos_list'),
    path('sexos/<int:id>', SexoView.as_view(), name='sexos_process'),
    path('estados/', EstadoView.as_view(), name='estados_list'),
    path('estados/<int:id>', EstadoView.as_view(), name='estados_process'),
    path('estudiantes/', EstudianteView.as_view(), name='estudiantes_list'),
    path('estudiantes/<int:id>', EstudianteView.as_view(), name='estudiantes_process'),
    path('catedraticos/', CatedraticoView.as_view(), name='catedraticos_list'),
    path('catedraticos/<int:id>', CatedraticoView.as_view(), name='catedraticos_process'),
    path('administrativos/', AdministrativoView.as_view(), name='administrativos_list'),
    path('administrativos/<int:id>', AdministrativoView.as_view(), name='administrativos_process'),
    ]