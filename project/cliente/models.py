from django.db import models

# Create your models here.


class Pais(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.nombre.capitalize()}"

    class Meta:
        verbose_name_plural = "País"
        verbose_name = "País"


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    pais = models.ForeignKey(
        Pais, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"

    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"
