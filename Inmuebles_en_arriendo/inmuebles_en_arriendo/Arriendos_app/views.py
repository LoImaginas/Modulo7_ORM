from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm, RegisterForm, ProfileForm, InmuebleForm
from django.contrib.auth.decorators import login_required
from .models import Usuario, Inmueble, TipoInmueble, Comuna, Region, InmuebleUsuario

def home(request):
    return render(request, 'inicio.html')

def profile(request):
    return render(request, 'perfil.html', {'user': request.user})

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redirige al perfil después de guardar los cambios
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'editar_perfil.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('perfil')  # Redirige al perfil después del login
    else:
        form = LoginForm()
    return render(request, 'iniciar_sesion.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciar_sesion') # Redirige a la página de login después del registro
    else:
        form = RegisterForm()
    return render(request, 'registrar.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    if hasattr(user, 'usuario'):
        user_type = user.usuario.tipo_usuario.nombre
    else:
        user_type = 'Desconocido'

    context = {
        'user': user,
        'user_type': user_type,
    }

    return render(request, 'perfil.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'editar_perfil.html', {'form': form})

@login_required
def create_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redirige al perfil después de crear el inmueble
    else:
        form = InmuebleForm()
    return render(request, 'crear_inmueble.html', {'form': form})

@login_required
def search_inmuebles(request):
    inmuebles = Inmueble.objects.all()  # Ajusta la búsqueda según tus necesidades
    return render(request, 'buscar_inmuebles.html', {'inmuebles': inmuebles})

