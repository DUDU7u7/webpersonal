from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_delete


class Prenda(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    imagen = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.nombre
    
@receiver(post_delete, sender=Prenda)
def eliminar_imagen_prenda(sender, instance, **kwargs):
    if instance.imagen:
        instance.imagen.delete(False)


class Categoria(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Talla(models.Model):
    talla = models.CharField(max_length=10)

    def __str__(self):
        return self.talla

class Color(models.Model):
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.color



class MetodoPago(models.Model):
    nombre_pago = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_pago

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    estado_pedido = models.CharField(max_length=50)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    direccion_envio = models.CharField(max_length=100)
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pedido {self.pk}'

# class CarritoCompra(models.Model):
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     prenda = models.ForeignKey(Prenda, on_delete=models.CASCADE)
#     cantidad_prenda = models.PositiveIntegerField()
#     fecha_hora = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Carrito {self.pk} de {self.usuario.username}'
