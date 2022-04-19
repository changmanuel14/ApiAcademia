import json
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Sexo, Estado, Estudiante, Catedratico, Administrativo
from .models import Curso, Ciclo, ClaseHeader, ClaseDesc, Emergencia
from .models import User, RequisitoCatedratico, RequisitoEstudiante, Requisito, TipoUsuario
import json

# Create your views here.

class SexoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            sexos = list(Sexo.objects.filter(id=id).values())
            sexos = sexos[0]
        else:
            sexos = list(Sexo.objects.values())

        if len(sexos) > 0:
            datos = {'message': 'success', 'sexos': sexos}
        else:
            datos = {'message': 'Datos no encontrados'}
        
        return JsonResponse(datos)
     
    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Sexo.objects.create(sexo = jd['sexo'])
        datos = {'message': 'success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        sexos = list(Sexo.objects.filter(id=id).values())
        if len(sexos) > 0:
            sexo = Sexo.objects.get(id=id)
            sexo.sexo = jd['sexo']
            sexo.save()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        
        return JsonResponse(datos)


    def delete(self, request, id):
        sexos = list(Sexo.objects.filter(id=id).values())
        if len(sexos) > 0:
            Sexo.objects.filter(id=id).delete()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)

class EstadoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            estados = list(Estado.objects.filter(id=id).values())
            estados = estados[0]
        else:
            estados = list(Estado.objects.values())

        if len(estados) > 0:
            datos = {'message': 'success', 'estados': estados}
        else:
            datos = {'message': 'Datos no encontrados'}
        
        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        Estado.objects.create(estado = jd['estado'])
        datos = {'message': 'success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        estados = list(Estado.objects.filter(id=id).values())
        if len(estados) > 0:
            estado = Estado.objects.get(id=id)
            estado.estado = jd['estado']
            estado.save()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        
        return JsonResponse(datos)

    def delete(self, request, id):
        estados = list(Estado.objects.filter(id=id).values())
        if len(estados) > 0:
            Estado.objects.filter(id=id).delete()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)

class EstudianteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            estudiantes = list(Estudiante.objects.filter(id=id).values())
            estudiantes = estudiantes[0]
        else:
            estudiantes = list(Estudiante.objects.values())

        if len(estudiantes) > 0:
            datos = {'message': 'success', 'estudiantes': estudiantes}
        else:
            datos = {'message': 'Datos no encontrados'}
        
        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        sexo = Sexo.objects.get(id=jd["sexo"])
        estado = Estado.objects.get(id=6)
        Estudiante.objects.create(nombre1 = jd['nombre1'], nombre2 = jd['nombre2'],
        nombre3 = jd['nombre3'], apellido1 = jd['apellido1'], apellido2 = jd['apellido2'],
        apellido3 = jd['apellido3'], sexo = sexo, fechanacimiento = jd['fechanacimiento'],
        direccion = jd['direccion'], foto = jd['foto'], cui = jd['cui'], 
        carnet = jd['carnet'], telefono1 = jd['telefono1'], telefono2 = jd['telefono2'],
        correo = jd['correo'], estado = estado)
        datos = {'message': 'success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        estudiantes = list(Estudiante.objects.filter(id=id).values())
        if len(estudiantes) > 0:
            sexo = list(Sexo.objects.filter(id=jd['sexo']).values())
            estado = list(Estado.objects.get(id=jd['estado']).values())
            sexo = sexo[0]
            estado = estado[0]
            estudiante = Estudiante.objects.get(id=id)
            estudiante.nombre1 = jd['nombre1']
            estudiante.nombre2 = jd['nombre2']
            estudiante.nombre3 = jd['nombre3']
            estudiante.apellido1 = jd['apellido1']
            estudiante.apellido2 = jd['apellido2']
            estudiante.apellido3 = jd['apellido3']
            estudiante.sexo = sexo
            estudiante.fechanacimiento = js['fechanacimiento']
            estudiante.direccion = jd['direccion']
            estudiante.foto = jd['foto']
            estudiante.cui = jd['cui'], 
            estudiante.carnet = jd['carnet']
            estudiante.telefono1 = jd['telefono1']
            estudiante.telefono2 = jd['telefono2'],
            estudiante.correo = jd['correo']
            estudiante.estado = estado
            estudiante.save()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        
        return JsonResponse(datos)

    def delete(self, request, id):
        estudiantes = list(Estudiante.objects.filter(id=id).values())
        if len(estudiantes) > 0:
            Estudiante.objects.filter(id=id).delete()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)