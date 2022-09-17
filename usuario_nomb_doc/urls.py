from django.urls import path
from usuario_nomb_doc.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #LOGIN
    path('login/', login_request, name='LoginUsuario'),   
    #LOGOUT 
    path('logout/', LogoutView.as_view(template_name='formularios/usuarios/logout.htmL'), name='LogoutUsuario'), 
]