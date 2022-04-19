from django.db import models

# Create your models here.

class Sexo(models.Model):
    sexo = models.CharField(max_length=20)

class Estado(models.Model):
    estado = models.CharField(max_length=50)

class Estudiante(models.Model):
    nombre1 = models.CharField(max_length=50)
    nombre2 = models.CharField(max_length=50, null=True)
    nombre3 = models.CharField(max_length=50, null=True)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50, null=True)
    apellido3 = models.CharField(max_length=50, null=True)
    sexo = models.ForeignKey(Sexo, on_delete=models.SET_NULL, null=True)
    fechanacimiento = models.DateField()
    foto = models.CharField(max_length=500, null=True)
    direccion = models.CharField(max_length=200)
    cui = models.CharField(max_length=13, null=True)
    carnet = models.CharField(max_length=13)
    telefono1 = models.PositiveIntegerField(null=True)
    telefono2 = models.PositiveIntegerField(null=True)
    correo = models.EmailField(null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)

class Administrativo(models.Model):
    nombre1 = models.CharField(max_length=50)
    nombre2 = models.CharField(max_length=50, null=True)
    nombre3 = models.CharField(max_length=50, null=True)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50, null=True)
    apellido3 = models.CharField(max_length=50, null=True)
    sexo = models.ForeignKey(Sexo, on_delete=models.SET_NULL, null=True)
    fechanacimiento = models.DateField()
    foto = models.CharField(max_length=500, null=True)
    direccion = models.CharField(max_length=200)
    cui = models.CharField(max_length=13, null=True)
    codigo = models.CharField(max_length=13)
    telefono1 = models.PositiveIntegerField(null=True)
    telefono2 = models.PositiveIntegerField(null=True)
    correo = models.EmailField(null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)

class Catedratico(models.Model):
    nombre1 = models.CharField(max_length=50)
    nombre2 = models.CharField(max_length=50, null=True)
    nombre3 = models.CharField(max_length=50, null=True)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50, null=True)
    apellido3 = models.CharField(max_length=50, null=True)
    sexo = models.ForeignKey(Sexo, on_delete=models.SET_NULL, null=True)
    fechanacimiento = models.DateField()
    foto = models.CharField(max_length=500, null=True)
    direccion = models.CharField(max_length=200)
    cui = models.CharField(max_length=13, null=True)
    codigo = models.CharField(max_length=13)
    telefono1 = models.PositiveIntegerField(null=True)
    telefono2 = models.PositiveIntegerField(null=True)
    correo = models.EmailField(null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    inscripcion = models.FloatField()
    mensualidad = models.FloatField()

class TipoUsuario(models.Model):
    tipousuario = models.CharField(max_length=50)

class Requisito(models.Model):
    requisito = models.CharField(max_length=200)
    tipousuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    
class RequisitoEstudiante(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.SET_NULL, null=True)
    requisito = models.ForeignKey(Requisito, on_delete=models.SET_NULL, null=True)
    url = models.CharField(max_length=300)

class RequisitoCatedratico(models.Model):
    catedratico = models.ForeignKey(Catedratico, on_delete=models.SET_NULL, null=True)
    requisito = models.ForeignKey(Requisito, on_delete=models.SET_NULL, null=True)
    url = models.CharField(max_length=300)

class Ciclo(models.Model):
    nombre = models.CharField(max_length=200)
    fechainicio = models.DateField()
    fechafin = models.DateField()
    activo = models.BooleanField()

class ClaseHeader(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    catedratico = models.ForeignKey(Catedratico, on_delete=models.SET_NULL, null=True)
    fechainicio = models.DateField()
    fechafin = models.DateField()
    cupo = models.PositiveIntegerField()
    activo = models.BooleanField()
    seccion = models.CharField(max_length=2)

class ClaseDesc(models.Model):
    header = models.ForeignKey(ClaseHeader, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.SET_NULL, null=True)
    nota = models.PositiveIntegerField(default=0)

class User(models.Model):
    user = models.CharField(max_length=30)
    administrativo = models.ForeignKey(Administrativo, on_delete=models.CASCADE)
    password = models.CharField(max_length=256)

class Emergencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=300)
    telefono = models.PositiveIntegerField()
