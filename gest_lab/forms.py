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

class FormularioMineria(forms.Form):

    Linfocitos = forms.CharField(required=True, label='Linfocitos', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    MID = forms.CharField(required=True, label='MID', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    Neutrofilos = forms.CharField(required=True, label='Neutrofilos', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    Leucocitos = forms.CharField(required=True, label='Leucocitos', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    Eritrocitos = forms.CharField(required=True, label='Eritrocitos', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    Hemoglobina = forms.CharField(required=True, label='Hemoglobina', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    Hematocritos = forms.CharField(required=True, label='Hematocritos', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    MCV = forms.CharField(required=True, label='MCV', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    MCH = forms.CharField(required=True, label='MCH', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    MCHC = forms.CharField(required=True, label='MCHC', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    Plaquetas = forms.CharField(required=True, label='Plaquetas', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    MPV = forms.CharField(required=True, label='MPV', widget=forms.TextInput(attrs={ 'class': 'form-control' }))