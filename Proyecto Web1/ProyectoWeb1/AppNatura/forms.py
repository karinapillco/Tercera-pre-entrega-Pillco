from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Perfumeformulario(forms.Form):

    nombre = forms.CharField(max_length=50)
    contenido_neto = forms.IntegerField()
    vto = forms.DateField()
    precio = forms.FloatField()

class Corporalformulario(forms.Form):

    nombre = forms.CharField(max_length=50)
    contenido_neto = forms.IntegerField()
    vto = forms.DateField()
    precio = forms.FloatField()

class RegistrarUsuario(UserCreationForm):
    username = forms.CharField(label="ingrese su nombre de usuario")
    email = forms.EmailField(label="Correo elctronico")
    password1 = forms.CharField(label="Ingrese su contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme su contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Ingrese su nombre")
    last_name = forms.CharField(label="Ingrese su apellido")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]