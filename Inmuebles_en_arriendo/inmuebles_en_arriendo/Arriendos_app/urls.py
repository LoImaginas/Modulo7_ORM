from django.urls import path
from .views import obtener_comunas, user_login, register, profile, edit_profile, home, create_inmueble, editar_inmueble,eliminar_inmueble, lista_inmuebles, mis_inmuebles, enviar_mensaje
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='inicio'),
    path('login/', user_login, name='iniciar_sesion'),
    path('register/', register, name='registrar'),
    path('profile/', profile, name='perfil'),
    path('edit_profile/', edit_profile, name='editar_perfil'),
    path('inmuebles/nuevo/', create_inmueble, name='crear_inmueble'),
    path('inmuebles/editar/<int:id>/', editar_inmueble, name='editar_inmueble'),
    path('inmuebles/eliminar/<int:id>/', eliminar_inmueble, name='eliminar_inmueble'),
    path('inmuebles/', lista_inmuebles, name='lista_inmuebles'),
    path('contacto/<int:inmueble_id>/', enviar_mensaje, name='enviar_mensaje'),
    path('comunas/', obtener_comunas, name='obtener_comunas'),
    path('mis_inmuebles/', mis_inmuebles, name='mis_inmuebles'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    
]