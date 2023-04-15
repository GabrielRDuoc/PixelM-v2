from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='id de Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')

    

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre del Producto')

    def __str__(self):
        return self.nombreProducto