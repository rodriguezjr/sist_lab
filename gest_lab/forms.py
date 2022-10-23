from django import forms
from gest_lab.models import Cliente, Sexo
import datetime

class FormularioCliente(forms.ModelForm):
    sexo=forms.ModelChoiceField(queryset=Sexo.objects.all(), label='Sexo', widget=forms.RadioSelect())
    cedula = forms.CharField(required=True, label='Cedula', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    nombre = forms.CharField(required=True, label='Nombre', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    apellido = forms.CharField(required=True, label='Apellido', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    # f_nac = forms.DateField(required=True, label='Fecha de Nacimiento', widget=forms.SelectDateWidget(attrs={ 'class': 'form-control', 'type':'date'}))
    f_nac = forms.DateField(required=True, label='Fecha de Nacimiento', widget=forms.TextInput(attrs={ 'class': 'form-control', 'type':'date'}))
    direccion = forms.CharField(required=True, label='Direccion', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    telefono = forms.CharField(label='Telefono', widget=forms.TextInput(attrs={ 'class': 'form-control' }))


    class Meta():
        model = Cliente
        fields =['cedula','nombre','apellido','f_nac','direccion','telefono','sexo']