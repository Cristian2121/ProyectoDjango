from django.db import models
from django.contrib.auth import get_user_model

Usuario = get_user_model()

# Create your models here.
class Producto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='producto')
    precio = models.FloatField()
    cantidad = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)