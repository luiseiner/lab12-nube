from django.db import models


# Create your models here.


class Alumno(models.Model):
    codigo_a = models.CharField(primary_key=True, max_length=6)
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    fecha_nac = models.DateField()
    foto = models.ImageField(upload_to='imagenes/', blank=True)  # Campo para la imagen


    def __str__(self):
        texto="{0}{1}"
        return texto.format(self.codigo_a,self.apellido,self.nombre,self.correo,self.fecha_nac,self.foto)
