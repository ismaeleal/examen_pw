from django.db import models

# Create your models here.


class Circuscricion(models.Model):
	nombre = models.CharField(max_length=200)
	numero = models.IntegerField(max_length=200)

class Mesa(models.Model):
	nombre = models.CharField(max_length=200)
	circuscricion = models.ForeignKey(Circuscricion)


	def __str__(self):
		return self.nombre


	def __str__(self):
		return self.nombre
class Partido(models.Model):
	nombre = models.CharField(max_length=200)
	

	def __str__(self):
		return self.nombre

class Resultado(models.Model):
	partido = models.ForeignKey(Partido)
	mesa = models.ForeignKey(Mesa)

	def __str__(self):
		return self.partido

