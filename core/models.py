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
    

    class Usuario(models.Model):
        idUsuario=models.IntegerField(primary_key=True, verbose_name='id de usuario')
        Nombre = models.CharField(max_length=50, verbose_name='Nombre del usuario')
        Apellido = models.CharField(max_length=50, verbose_name='Apellido del usuario')
        Correo =  models.CharField(max_length=50, verbose_name='Correo')
        Direccion = models.CharField(max_length=50, verbose_name='Direccion del usuario')
        Contraseña = models.CharField(max_length=50, verbose_name='Contraseña')
        def __str__(self):
            return self.Nombre