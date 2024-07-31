from django.urls import path
from .views import user_login, register, profile, edit_profile, home, create_inmueble, search_inmuebles
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', home, name='inicio'), # Pagina de inicio 
    path('login/', user_login, name='iniciar_sesion'), #iniciar sesion
    path('register/', register, name='registrar'), #registro
    path('profile/', profile, name='perfil'), #perfil
    path('edit_profile/', edit_profile, name='editar_perfil'), #editar perfil 
    path('create_inmueble/', create_inmueble, name='crear_inmueble'),
    path('search_inmuebles/', search_inmuebles, name='buscar_inmuebles'),
    path('logout/', LogoutView.as_view(), name='logout'),
]