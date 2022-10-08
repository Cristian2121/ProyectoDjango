from dataclasses import fields
from django import forms

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    imagen = forms.ImageField(required=False)
    precio = forms.FloatField()
    cantidad = forms.IntegerField()    