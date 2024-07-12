from django.contrib import admin

# Register your models here.
from TiendaVirtual.models import  Categoria, Color, MetodoPago, Pedido, Prenda, Talla

# admin.site.register(CarritoCompra)
admin.site.register(Categoria)
admin.site.register(Color)
admin.site.register(MetodoPago)
admin.site.register(Pedido)
admin.site.register(Prenda)
admin.site.register(Talla)