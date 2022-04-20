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
        try:
            Estudiante.objects.create(nombre1 = jd['nombre1'], nombre2 = jd['nombre2'],
            nombre3 = jd['nombre3'], apellido1 = jd['apellido1'], apellido2 = jd['apellido2'],
            apellido3 = jd['apellido3'], sexo = sexo, fechanacimiento = jd['fechanacimiento'],
            direccion = jd['direccion'], foto = jd['foto'], cui = jd['cui'], 
            carnet = jd['carnet'], telefono1 = jd['telefono1'], telefono2 = jd['telefono2'],
            correo = jd['correo'], estado = estado)
            datos = {'message': 'success'}
        except:
            datos = {'message': 'Operacion no completada'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        estudiantes = list(Estudiante.objects.filter(id=id).values())
        if len(estudiantes) > 0:
            sexo = Sexo.objects.get(id=jd["sexo"])
            estado = Estado.objects.get(id=jd['estado'])
            estudiante = Estudiante.objects.get(id=id)
            estudiante.nombre1 = jd['nombre1']
            estudiante.nombre2 = jd['nombre2']
            estudiante.nombre3 = jd['nombre3']
            estudiante.apellido1 = jd['apellido1']
            estudiante.apellido2 = jd['apellido2']
            estudiante.apellido3 = jd['apellido3']
            estudiante.sexo = sexo
            estudiante.fechanacimiento = jd['fechanacimiento']
            estudiante.direccion = jd['direccion']
            estudiante.foto = jd['foto']
            estudiante.cui = jd['cui']
            estudiante.carnet = jd['carnet']
            estudiante.telefono1 = jd['telefono1']
            estudiante.telefono2 = jd['telefono2']
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

class CatedraticoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            catedraticos = list(Catedratico.objects.filter(id=id).values())
            catedraticos = catedraticos[0]
        else:
            catedraticos = list(Catedratico.objects.values())

        if len(catedraticos) > 0:
            datos = {'message': 'success', 'catedraticos': catedraticos}
        else:
            datos = {'message': 'Datos no encontrados'}
        
        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        sexo = Sexo.objects.get(id=jd["sexo"])
        estado = Estado.objects.get(id=2)
        try:
            Catedratico.objects.create(nombre1 = jd['nombre1'], nombre2 = jd['nombre2'],
            nombre3 = jd['nombre3'], apellido1 = jd['apellido1'], apellido2 = jd['apellido2'],
            apellido3 = jd['apellido3'], sexo = sexo, fechanacimiento = jd['fechanacimiento'],
            direccion = jd['direccion'], foto = jd['foto'], cui = jd['cui'], 
            codigo = jd['codigo'], telefono1 = jd['telefono1'], telefono2 = jd['telefono2'],
            correo = jd['correo'], estado = estado)
            datos = {'message': 'success'}
        except:
            datos = {'message': 'Operacion no completada'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        catedraticos = list(Catedratico.objects.filter(id=id).values())
        if len(catedraticos) > 0:
            sexo = Sexo.objects.get(id=jd["sexo"])
            estado = Estado.objects.get(id=jd['estado'])
            catedratico = Catedratico.objects.get(id=id)
            catedratico.nombre1 = jd['nombre1']
            catedratico.nombre2 = jd['nombre2']
            catedratico.nombre3 = jd['nombre3']
            catedratico.apellido1 = jd['apellido1']
            catedratico.apellido2 = jd['apellido2']
            catedratico.apellido3 = jd['apellido3']
            catedratico.sexo = sexo
            catedratico.fechanacimiento = jd['fechanacimiento']
            catedratico.direccion = jd['direccion']
            catedratico.foto = jd['foto']
            catedratico.cui = jd['cui']
            catedratico.codigo = jd['codigo']
            catedratico.telefono1 = jd['telefono1']
            catedratico.telefono2 = jd['telefono2']
            catedratico.correo = jd['correo']
            catedratico.estado = estado
            catedratico.save()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)

    def delete(self, request, id):
        catedraticos = list(Catedratico.objects.filter(id=id).values())
        if len(catedraticos) > 0:
            Catedratico.objects.filter(id=id).delete()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)

class AdministrativoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            administrativos = list(Administrativo.objects.filter(id=id).values())
            administrativos = administrativos[0]
        else:
            administrativos = list(Administrativo.objects.values())

        if len(administrativos) > 0:
            datos = {'message': 'success', 'administrativos': administrativos}
        else:
            datos = {'message': 'Datos no encontrados'}
        
        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        sexo = Sexo.objects.get(id=jd["sexo"])
        estado = Estado.objects.get(id=2)
        try:
            Administrativo.objects.create(nombre1 = jd['nombre1'], nombre2 = jd['nombre2'],
            nombre3 = jd['nombre3'], apellido1 = jd['apellido1'], apellido2 = jd['apellido2'],
            apellido3 = jd['apellido3'], sexo = sexo, fechanacimiento = jd['fechanacimiento'],
            direccion = jd['direccion'], foto = jd['foto'], cui = jd['cui'], 
            codigo = jd['codigo'], telefono1 = jd['telefono1'], telefono2 = jd['telefono2'],
            correo = jd['correo'], estado = estado)
            datos = {'message': 'success'}
        except:
            datos = {'message': 'Operacion no completada'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        administrativos = list(Administrativo.objects.filter(id=id).values())
        if len(administrativos) > 0:
            sexo = Sexo.objects.get(id=jd["sexo"])
            estado = Estado.objects.get(id=jd['estado'])
            administrativo = Administrativo.objects.get(id=id)
            administrativo.nombre1 = jd['nombre1']
            administrativo.nombre2 = jd['nombre2']
            administrativo.nombre3 = jd['nombre3']
            administrativo.apellido1 = jd['apellido1']
            administrativo.apellido2 = jd['apellido2']
            administrativo.apellido3 = jd['apellido3']
            administrativo.sexo = sexo
            administrativo.fechanacimiento = jd['fechanacimiento']
            administrativo.direccion = jd['direccion']
            administrativo.foto = jd['foto']
            administrativo.cui = jd['cui']
            administrativo.codigo = jd['codigo']
            administrativo.telefono1 = jd['telefono1']
            administrativo.telefono2 = jd['telefono2']
            administrativo.correo = jd['correo']
            administrativo.estado = estado
            administrativo.save()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)

    def delete(self, request, id):
        administrativos = list(Administrativo.objects.filter(id=id).values())
        if len(administrativos) > 0:
            Administrativo.objects.filter(id=id).delete()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)

class CursoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            cursos = list(Curso.objects.filter(id=id).values())
            cursos = cursos[0]
        else:
            cursos = list(Curso.objects.values())

        if len(cursos) > 0:
            datos = {'message': 'success', 'cursos': cursos}
        else:
            datos = {'message': 'Datos no encontrados'}
        
        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        try:
            Curso.objects.create(nombre = jd['nombre'], inscripcion = jd['inscripcion'], mensualidad = jd['mensualidad'])
            datos = {'message': 'success'}
        except:
            datos = {'message': 'Operacion no completada'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        cursos = list(Curso.objects.filter(id=id).values())
        if len(cursos) > 0:
            curso = Curso.objects.get(id=id)
            curso.nombre = jd['nombre']
            curso.inscripcion = jd['inscripcion']
            curso.mensualidad = jd['mensualidad']
            curso.save()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)

    def delete(self, request, id):
        cursos = list(Curso.objects.filter(id=id).values())
        if len(cursos) > 0:
            Curso.objects.filter(id=id).delete()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)

class CicloView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            ciclos = list(Ciclo.objects.filter(id=id).values())
            ciclos = ciclos[0]
        else:
            ciclos = list(Ciclo.objects.values())

        if len(cursos) > 0:
            datos = {'message': 'success', 'ciclos': ciclos}
        else:
            datos = {'message': 'Datos no encontrados'}
        
        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        try:
            Ciclo.objects.create(nombre = jd['nombre'], fechainicio = jd['fechainicio'], fechafin = jd['fechafin'], activo = True)
            datos = {'message': 'success'}
        except:
            datos = {'message': 'Operacion no completada'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        ciclos = list(Ciclo.objects.filter(id=id).values())
        if len(ciclos) > 0:
            ciclo = Ciclo.objects.get(id=id)
            ciclo.nombre = jd['nombre']
            ciclo.fechainicio = jd['fechainicio']
            ciclo.fechafin = jd['fechafin']
            ciclo.activo = jd['activo']
            curso.save()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)

    def delete(self, request, id):
        ciclos = list(Ciclo.objects.filter(id=id).values())
        if len(ciclos) > 0:
            Ciclo.objects.filter(id=id).delete()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)

class ClaseHeaderView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            cheaders = list(ClaseHeader.objects.filter(id=id).values())
            cheaders = cheaders[0]
        else:
            cheaders = list(ClaseHeader.objects.values())

        if len(cursos) > 0:
            datos = {'message': 'success', 'cheaders': cheaders}
        else:
            datos = {'message': 'Datos no encontrados'}
        
        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        try:
            catedratico = Catedratico.objects.get(id=jd['catedratico'])
            curso = Curso.objects.get(id=jd['curso'])
            ciclo = Ciclo.objects.get(id=jd['ciclo'])
            ClaseHeader.objects.create(fechainicio = jd['fechainicio'], fechafin = jd['fechafin'], cupo = jd['cupo'], activo = True, 
            seccion = jd['seccion'], catedratico = catedratico, curso = curso, ciclo = ciclo)
            datos = {'message': 'success'}
        except:
            datos = {'message': 'Operacion no completada'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        cheaders = list(ClaseHeader.objects.filter(id=id).values())
        if len(cheaders) > 0:
            catedratico = Catedratico.objects.get(id=jd['catedratico'])
            curso = Curso.objects.get(id=jd['curso'])
            ciclo = Ciclo.objects.get(id=jd['ciclo'])
            cheader = ClaseHeader.objects.get(id=id)
            cheader.curso = curso
            cheader.ciclo = ciclo
            cheader.catedratico = catedratico
            cheader.fechainicio = jd['fechainicio']
            cheader.fechafin = jd['fechafin']
            cheader.cupo = jd['cupo']
            cheader.activo = jd['activo']
            cheader.seccion = jd['seccion']
            cheader.save()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)

    def delete(self, request, id):
        cheaders = list(ClaseHeader.objects.filter(id=id).values())
        if len(cheaders) > 0:
            ClaseHeader.objects.filter(id=id).delete()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)

class ClaseDescView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            cdescs = list(ClaseDesc.objects.filter(id=id).values())
            cdescs = cdescs[0]
        else:
            cdescs = list(ClaseDesc.objects.values())

        if len(cursos) > 0:
            datos = {'message': 'success', 'cdescs': cdescs}
        else:
            datos = {'message': 'Datos no encontrados'}
        
        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        try:
            header = ClaseHeader.objects.get(id=jd['header'])
            estudiante = Estudiante.objects.get(id=jd['estudiante'])
            ClaseDesc.objects.create(nota = 0, header = header, estudiante = estudiante)
            datos = {'message': 'success'}
        except:
            datos = {'message': 'Operacion no completada'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        cdescs = list(ClaseDesc.objects.filter(id=id).values())
        if len(cdescs) > 0:
            header = ClaseHeader.objects.get(id=jd['header'])
            estudiante = Estudiante.objects.get(id=jd['estudiante'])
            cdescs = ClaseDesc.objects.get(id=id)
            cdescs.header = header
            cdescs.estudiante = estudiante
            cdescs.nota = jd['nota']
            cdescs.save()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)

    def delete(self, request, id):
        cdescs = list(ClaseDesc.objects.filter(id=id).values())
        if len(cdescs) > 0:
            ClaseDesc.objects.filter(id=id).delete()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)

class EmergenciaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            emergencias = list(Emergencia.objects.filter(id=id).values())
            emergencias = emergencias[0]
        else:
            emergencias = list(Emergencia.objects.values())

        if len(cursos) > 0:
            datos = {'message': 'success', 'emergencias': emergencias}
        else:
            datos = {'message': 'Datos no encontrados'}
        
        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        try:
            estudiante = Estudiante.objects.get(id=jd['estudiante'])
            Emergencia.objects.create(estudiante = estudiante, nombre = jd['nombre'], apellido = jd['apellido'], telefono = jd['telefono'])
            datos = {'message': 'success'}
        except:
            datos = {'message': 'Operacion no completada'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        emergencias = list(ClaseDesc.objects.filter(id=id).values())
        if len(emergencias) > 0:
            estudiante = Estudiante.objects.get(id=jd['estudiante'])
            emergencias = Emergencia.objects.get(id=id)
            emergencias.estudiante = estudiante
            emergencias.nombre = jd['nombre']
            emergencias.apellido = jd['apellido']
            emergencias.telefono = jd['telefono']
            emergencias.save()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)

    def delete(self, request, id):
        emergencias = list(Emergencia.objects.filter(id=id).values())
        if len(emergencias) > 0:
            Emergencia.objects.filter(id=id).delete()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Datos no encontrados'}
        return JsonResponse(datos)

