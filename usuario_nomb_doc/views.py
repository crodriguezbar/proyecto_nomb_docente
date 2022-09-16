from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

#LOGIN
def login_request (request):
    formulario =AuthenticationForm(request, data=request.POST)
    if request.method == 'POST':
        data =formulario.cleaned_data
        if formulario.is_valid():
            usuario = data.get('username')
            contrasenia = data.get('password')
            user = authenticate(username = usuario, password = contrasenia)
            
            if user:
                login(request, user)
                messages.info (request, 'Bienvenido !')
            else:               
                messages.info (request, 'Inicio de sesion fallido !')
     
        else:               
            messages.info (request, 'Inicio de sesion fallido !')
        return redirect('XXXX')
    contexto={
        'formulario': AuthenticationForm(),
        'name_submit': 'login' 
    }
    return render (request, 'formularios/usuarios/login.html', contexto)  

