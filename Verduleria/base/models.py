from email.policy import default
from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    dni = models.IntegerField(default=0)

    def __str__(self):
        txt = "{0} {1} {2}"
        return txt.format(self.nombre, self.apellido, self.dni)


PRODUCTO_TIPO = [(1,'Fruta'), (2, 'Verdura')]


class Producto(models.Model):
    tipo = models.IntegerField(choices=PRODUCTO_TIPO, default='fruta')
    nombre = models.CharField(max_length=25)
    precio = models.IntegerField(default=0)
   

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.tipo, self.nombre,self.precio)


class Compra(models.Model):
    cliente = models.ForeignKey(Cliente,null = True , blank=False, on_delete=models.CASCADE)
    hora = models.DateTimeField(null=False)
    
    def __str__(self):
        return f'{self.cliente} {self.hora}'

class Detalle(models.Model):
    producto = models.ForeignKey(Producto,null = False , blank=False, on_delete = models.CASCADE)
    compra = models.ForeignKey(Compra, null=False,blank=False, on_delete = models.CASCADE)
    preciokg = models.IntegerField(default=0)
  


    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.producto, self.compra, self.preciokg)

