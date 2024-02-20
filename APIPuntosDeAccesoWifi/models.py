from django.db import models

# Create your models here.


class WifiAccesPoint(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    programa = models.CharField(max_length=50)
    fecha_instalacion = models.DateField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    colonia = models.CharField(max_length = 100)
    alcaldia = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.id
