from django.urls import path
from .views import SexoView, EstadoView, EstudianteView, CatedraticoView, AdministrativoView, CicloView
from .views import CursoView, ClaseHeaderView, ClaseDescView, EmergenciaView

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
    path('cursos/', CursoView.as_view(), name='cursos_list'),
    path('cursos/<int:id>', CursoView.as_view(), name='cursos_process'),
    path('ciclos/', CicloView.as_view(), name='ciclos_list'),
    path('ciclos/<int:id>', CicloView.as_view(), name='ciclos_process'),
    path('cheaders/', ClaseHeaderView.as_view(), name='cheaders_list'),
    path('cheaders/<int:id>', ClaseHeaderView.as_view(), name='cheaders_process'),
    path('cdescs/', ClaseDescView.as_view(), name='cdescs_list'),
    path('cdescs/<int:id>', ClaseDescView.as_view(), name='cdescs_process'),
    path('emergencias/', EmergenciaView.as_view(), name='emergencias_list'),
    path('emergencias/<int:id>', EmergenciaView.as_view(), name='emergencias_process'),
    ]