from django import forms

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
