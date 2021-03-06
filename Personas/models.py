import datetime

from django.db import models

# Create your models here.
class Lugar(models.Model):
    manager = models.ForeignKey('self', null=True,blank=True, related_name="lugares",on_delete=models.CASCADE)
    nombre=models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    lugar=models.ForeignKey(Lugar, on_delete=models.CASCADE)
    cedula=models.CharField(max_length=10)
    nombres=models.CharField(max_length=60)
    apellidos=models.CharField(max_length=60)
    fecha_nacimiento=models.DateField()
    edad=models.IntegerField(default=0)
    estado_civil=models.CharField(max_length=30, choices=(("Soltero","Soltero"),("Casado","Casado"),("Viudo","Viudo"),("Divorciado","Divorciado"),),null=True,blank=True)
    sexo=models.CharField(max_length=30, choices=(("Masculino","Masculino"),("Femenino","Femenino")),null=True,blank=True)
    telefono=models.CharField(max_length=13,default="0000000000")
    def __str__(self):
        return "%s %s"%(self.nombres, self.apellidos)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.edad=datetime.datetime.now().year - self.fecha_nacimiento.year
        super(Persona, self).save()

