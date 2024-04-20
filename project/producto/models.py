from django.db import models

# Create your models here.


class ProductoCategoria(models.Model):
    """Categorías de Productos"""
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="Descripción")

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorías de Productos"
        verbose_name = "Categoría de Producto"
