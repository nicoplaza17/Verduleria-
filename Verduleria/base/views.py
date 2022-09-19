from django.shortcuts import render, redirect
from .models import Compra,Cliente
from .forms import CompraForm,ClienteForm
# Create your views here.



def comprar(request):

    
    form = CompraForm()
    context = {'form':form}
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('home')
    
    return render(request,'compra.html',context)

def inicio(request):
    
    if request.method == 'POST':
        return redirect('compra')
        
        
    return render(request, 'inicio.html')
    
def factura(request):
    return render(request, 'factura.html')