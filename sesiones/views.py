from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.
class InicioSesion(View):
    def get(self, request):
        formulario_crear = UserCreationForm()
        formulario_iniciar = AuthenticationForm()

        return render(request, 'sesiones/inicio_sesion.html', {'form_crear':formulario_crear, 'form_iniciar':formulario_iniciar})

    def post(self, request, opcion):
        if opcion == 1:
            form_crear = UserCreationForm(request.POST)
            
            if form_crear.is_valid():
                # save() retorna la instancia del modelo registrado
                usuario = form_crear.save()

                login(request, usuario)

                return redirect('inventario')  
            else:
                return redirect('error_inicio')
        elif opcion == 2:
            form_iniciar = AuthenticationForm(request, request.POST)

            if form_iniciar.is_valid():
                # save() retorna la instancia del modelo registrado
                usuario = form_iniciar.cleaned_data['username']
                contrasenia = form_iniciar.cleaned_data['password']

                verif_usuario = authenticate(username=usuario, password=contrasenia)

                if verif_usuario is not None:
                    print('SI ESTOY AQUI')
                    login(request, verif_usuario)

                    return redirect('inventario')            
                else:
                    return redirect('error_inicio')
        else:
            return redirect('error_inicio')

def error_inicio(request):
    mensaje = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Error</title>
        </head>
        <body>
            <h1>ha ocurrido un error. Pruebe de nuevo.</h1>
            <br />
            <a href="/">Volver a Iniciar sesión</a>
        </body>
        </html>
    """

    return HttpResponse(mensaje)