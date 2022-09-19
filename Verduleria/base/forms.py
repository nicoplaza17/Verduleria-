from django.forms import ModelForm
from .models import Compra,Cliente

class CompraForm(ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
