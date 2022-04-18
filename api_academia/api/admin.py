from django.contrib import admin
from .models import Sexo, Estado, Estudiante, Catedratico, Administrativo
from .models import Curso, Ciclo, ClaseHeader, ClaseDesc, Emergencia
from .models import User, RequisitoCatedratico, RequisitoEstudiante, Requisito, TipoUsuario
# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Sexo)
admin.site.register(Curso)
admin.site.register(Ciclo)
admin.site.register(ClaseHeader)
admin.site.register(ClaseDesc)
admin.site.register(Emergencia)
admin.site.register(Requisito)
admin.site.register(RequisitoEstudiante)
admin.site.register(RequisitoCatedratico)
admin.site.register(Catedratico)
admin.site.register(Administrativo)
admin.site.register(User)
admin.site.register(Estado)
admin.site.register(TipoUsuario)