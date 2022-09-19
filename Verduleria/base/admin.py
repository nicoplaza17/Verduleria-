from django.contrib import admin
from base.models import Cliente, Producto, Compra, Detalle
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Datos', {
            'fields': ('nombre', 'apellido', 'dni')

        }),
    )
    search_fields = ['nombre','apellido',"dni"]
    list_display = ['nombre','apellido',"dni"]


class ProductoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Datos', {
            'fields': ('tipo', "nombre","precio")

        }),
    )
    search_fields = ['nombre','precio']
    list_display = ['nombre',"precio"]




class CompraAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Datos', {
            'fields': ('cliente',"hora",)

        }),
    )
    search_fields = ['cliente','hora']
    list_display = ['cliente',"hora",]


class DetalleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Datos', {
            'fields': ('producto','compra',"preciokg")

        }),
    )
    search_fields = ['producto','compra',]
    list_display = ['producto','compra',"preciokg"]



admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Compra,CompraAdmin)
admin.site.register(Detalle,DetalleAdmin)



# Register your models here.
