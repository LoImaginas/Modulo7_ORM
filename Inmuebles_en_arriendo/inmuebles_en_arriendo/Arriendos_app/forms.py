from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, User
from .models import Usuario, Inmueble

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        }

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'nombre', 
            'descripcion', 
            'm2_construidos', 
            'm2_terreno', 
            'estacionamientos', 
            'habitaciones', 
            'banos', 
            'direccion', 
            'comuna', 
            'tipo_inmueble', 
            'precio_arriendo'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'm2_construidos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'M2 Construidos'}),
            'm2_terreno': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'M2 Terreno'}),
            'estacionamientos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Estacionamientos'}),
            'habitaciones': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Habitaciones'}),
            'banos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Baños'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'tipo_inmueble': forms.Select(attrs={'class': 'form-control'}),
            'precio_arriendo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio Arriendo'}),
        }
        