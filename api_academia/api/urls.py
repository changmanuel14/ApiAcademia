from django.urls import path
from .views import SexoView, EstadoView

urlpatterns =[
    path('sexos/', SexoView.as_view(), name='sexos_list'),
    path('estados/', EstadoView.as_view(), name='estados_list'),
    path('sexos/<int:id>', SexoView.as_view(), name='sexos_process'),
    path('estados/<int:id>', EstadoView.as_view(), name='estados_process'),
    ]