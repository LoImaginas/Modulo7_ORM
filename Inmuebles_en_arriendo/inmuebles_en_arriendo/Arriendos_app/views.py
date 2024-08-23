from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, login
from .forms import LoginForm, RegisterForm, ProfileForm, InmuebleForm, ContactoForm
from django.contrib.auth.decorators import login_required
from .models import Usuario, Inmueble, TipoInmueble, Comuna, Region, InmuebleUsuario, Contacto
from django.http import JsonResponse
from django.contrib.auth.views import LogoutView
from django.contrib import messages

def home(request):
    return render(request, 'inicio.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()  # Asegúrate de que este método esté actualizado
            auth_login(request, user)
            return redirect('perfil')  # Redirige al perfil después del login
    else:
        form = LoginForm()
    return render(request, 'iniciar_sesion.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente después del registro
            messages.success(request, 'Usuario creado exitosamente. Ahora puedes iniciar sesión.')
            return redirect('iniciar_sesion')  # Redirige a la vista del perfil
    else:
        form = RegisterForm()
    
    return render(request, 'registrar.html', {'form': form})

@login_required
def profile(request):
    usuario = request.user.usuario  # Accede al perfil asociado
    if usuario.tipo_usuario == 'arrendador':
        return render(request, 'perfil_arrendador.html', {'usuario': usuario})
    elif usuario.tipo_usuario == 'arrendatario':
        return render(request, 'perfil_arrendatario.html', {'usuario': usuario})
    else:
        return render(request, 'perfil.html', {'usuario': usuario})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.usuario)  # Cambia a usuario
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ProfileForm(instance=request.user.usuario)  # Cambia a usuario
    return render(request, 'editar_perfil.html', {'form': form})

@login_required
def create_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.propietario = request.user
            inmueble.save()
            return redirect('mis_inmuebles')
    else:
        form = InmuebleForm()
    return render(request, 'crear_inmueble.html', {'form': form})

def lista_inmuebles(request):
    query = request.GET.get('query', '')
    region_id = request.GET.get('region', '')
    comuna_id = request.GET.get('comuna', '')

    inmuebles = Inmueble.objects.all()

    if query:
        inmuebles = inmuebles.filter(nombre__icontains=query)
    
    if region_id:
        inmuebles = inmuebles.filter(comuna__region_id=region_id)

    if comuna_id:
        inmuebles = inmuebles.filter(comuna_id=comuna_id)
    
    regiones = Region.objects.all()
    comunas = Comuna.objects.filter(region_id=region_id) if region_id else Comuna.objects.none()

    return render(request, 'lista_inmuebles.html', {
        'inmuebles': inmuebles,
        'regiones': regiones,
        'comunas': comunas,
    })

@login_required
def editar_inmueble(request, id):
    inmueble = Inmueble.objects.get(id=id)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = InmuebleForm(instance=inmueble)
    
    return render(request, 'editar_inmueble.html', {'form': form})

@login_required
def eliminar_inmueble(request, id):
    inmueble = Inmueble.objects.get(id=id)
    if request.method == 'POST':
        inmueble.delete()
        return redirect('lista_inmuebles')  # Redirige a la lista de inmuebles después de la eliminación
    
    return render(request, 'confirmar_eliminar_inmueble.html', {'inmueble': inmueble})

@login_required
def mis_inmuebles(request):
    inmuebles = InmuebleUsuario.objects.filter(usuario=request.user.usuario).values_list('inmueble', flat=True)  # Cambia a usuario
    inmuebles_list = Inmueble.objects.filter(id__in=inmuebles)
    
    consultas = Contacto.objects.filter(inmueble__in=inmuebles_list)

    context = {
        'inmuebles': inmuebles_list,
        'consultas': consultas,
    }
    
    return render(request, 'mis_inmuebles.html', context)


@login_required
def enviar_mensaje(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    destinatario = inmueble.inmuebleusuario_set.first().usuario  # Suponiendo que el arrendador es el usuario asociado al inmueble

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            mensaje = form.cleaned_data['mensaje']
            Contacto.objects.create(
                inmueble=inmueble,
                remitente=request.user,
                destinatario=destinatario,
                mensaje=mensaje
            )
            return redirect('lista_inmuebles')
    else:
        form = ContactoForm()
    
    return render(request, 'enviar_mensaje.html', {'form': form, 'inmueble': inmueble})

def obtener_comunas(request):
    region_id = request.GET.get('region')
    comunas = Comuna.objects.filter(region_id=region_id) if region_id else Comuna.objects.none()
    data = {
        'comunas': list(comunas.values('id', 'nombre'))
    }
    return JsonResponse(data)

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Has cerrado sesión correctamente.")
        return super().dispatch(request, *args, **kwargs)