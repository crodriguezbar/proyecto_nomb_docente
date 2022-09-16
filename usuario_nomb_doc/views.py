from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

#LOGIN
def login_request (request):
    if request.method == 'POST':
        formulario =AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            data =formulario.cleaned_data
            usuario = data.get('username')
            contrasenia = data.get('password')
            user = authenticate(username = usuario, password = contrasenia)
            
            if user:
                login(request, user)
                messages.info (request, 'Bienvenido !')
            else:               
                messages.info (request, 'El usuario o contraseña es incorrecto !')
     
        else:               
            messages.info (request, 'Inicio de sesion fallido !')
        return redirect('LoginUsuario')
    contexto={
        'formulario': AuthenticationForm(),
    }
    return render (request, 'formularios/usuarios/login.html', contexto)  

