from django import forms 
from django.contrib.auth.forms import User
from .models import Usuario, Inmueble
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def get_user(self):
        email = self.cleaned_data.get('email')
        return authenticate(email=email, password=self.cleaned_data.get('password'))

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'rut', 'direccion', 'telefono_personal', 'email', 'tipo_usuario']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telefono_personal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'email', 'direccion', 'telefono_personal']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telefono_personal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
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
   
class ContactoForm(forms.Form):
    mensaje = forms.CharField(widget=forms.Textarea, max_length=1000)