from django.contrib.auth import logout, get_user_model
from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def inventario(request):
    usuario_iniciado = request.user.id

    productos = Producto.objects.filter(usuario=usuario_iniciado)

    contexto = {
        'productos':productos
    }

    return render(request, 'crud/inventario.html', context=contexto)

def crear_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)

        if formulario.is_valid():
            # Si entro al formulario
            datos = formulario.cleaned_data

            producto = Producto(
                usuario=request.user,
                nombre=datos['nombre'],
                imagen=datos['imagen'],
                precio=datos['precio'],
                cantidad=datos['cantidad']
            )
            producto.save()

            return redirect('inventario')

        print(formulario.errors)

    formulario = ProductoForm()

    return render(request, 'crud/crear.html', {'form':formulario})

def ver(request, id_producto):
    producto = Producto.objects.get(id=id_producto)

    return render(request, 'crud/ver.html', {'producto':producto})

def modificar(request, id_producto):
    producto = Producto.objects.get(id=id_producto)

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)

        if formulario.is_valid():
            # Si entro al formulario
            datos = formulario.cleaned_data

            producto.usuario = request.user
            producto.nombre = datos['nombre']
            if datos['imagen'] is not None:
                producto.imagen = datos['imagen']
            producto.precio = datos['precio']
            producto.cantidad = datos['cantidad']
            producto.save()

            return redirect('inventario')
        
        print(formulario.errors)

    # Inciar el formulario con datos
    formulario = ProductoForm(
        initial={
            'nombre':producto.nombre,
            'imagen':producto.imagen,
            'precio':producto.precio,
            'cantidad':producto.cantidad
        }
    )

    return render(request, 'crud/modificar.html', {'form':formulario, 'producto':producto})

def eliminar(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    producto.delete()

    return redirect('inventario')

def cerrar_sesion(request):
    logout(request)

    return redirect('iniciar_sesion')