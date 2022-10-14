from django import forms
from gest_lab.models import cliente, sexo


class FormularioCliente(forms.ModelForm):
    id_sexo=forms.ModelChoiceField(queryset=sexo.objects.all(), label='Sexo', widget=forms.RadioSelect(attrs={ 'class': 'form-check-input'}))
    cedula = forms.CharField(required=True, label='Cedula', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    nombre = forms.CharField(required=True, label='Nombre', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    apellido = forms.CharField(required=True, label='Apellido', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    f_nac = forms.DateField(required=True, label='Fecha de Nacimiento', widget=forms.SelectDateWidget(attrs={ 'class': 'form-control d-inline-block' }))
    direccion = forms.CharField(required=True, label='Direccion', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    telefono = forms.CharField(label='Telefono', widget=forms.TextInput(attrs={ 'class': 'form-control' }))


    class Meta():
        model = cliente
        fields =['cedula','nombre','apellido','f_nac','direccion','telefono','id_sexo']