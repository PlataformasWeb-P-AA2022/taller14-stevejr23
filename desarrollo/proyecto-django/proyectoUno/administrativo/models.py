from secrets import choice
from django.db import models

# Create your models here.


class Propietario(models.Model):
    #tipo = {'ecuatoriana', 'peruana', 'colombia'}
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField('edad')
    nacionalidad = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s %d %s" % (self.nombre,
                                self.apellido,
                                self.edad,
                                self.nacionalidad)


class Departamento(models.Model):
    costo_depa = models.FloatField('costo')
    num_cuartos = models.IntegerField('cuartos')
    num_banios = models.IntegerField('baños')
    valor_alicuta = models.FloatField('cuota')
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
                                    related_name="propietarioss")

    def __str__(self):
        return "%d %d %d %d" % (self.costo_depa,
                          self.num_cuartos,
                          self.num_banios,
                          self.valor_alicuta)
