from django.urls import path
from usuario_nomb_doc.views import *

urlpatterns = [
    #LOGIN
    path('login/', login_request, name='LoginUsuario'),    
]