from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(AbstractUser):
    vip = models.BooleanField
    saldo = models.DecimalField(max_digits=14,decimal_places=2, default=1)
    
    def __str__(self):
        return str(self.username)

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    unidades = models.IntegerField()
    precio = models.DecimalField(max_digits=14, decimal_places=2, default=1)
    vip = models.BooleanField()
    
class Compra(models.Model):
    unidades = models.IntegerField()
    importe = models.DecimalField(max_digits=14, decimal_places=2, default=1)
    iva = models.DecimalField(max_digits=3, decimal_places=2, default=0.21)
    usuario = models.OneToOneField(Usuario, on_delete=models.PROTECT)
    nombre = models.OneToOneField(Producto, on_delete=models.PROTECT)
    vip = models.BooleanField()
    
class Marca(models.Model):
    nombre = models.CharField(max_length=200)    
