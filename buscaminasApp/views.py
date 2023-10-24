from django.shortcuts import render
from .forms import TableroForm

def crear_tablero(request):
    tablero = None

    if request.method == 'GET':
        form = TableroForm(request.GET)
        if form.is_valid():
            filas = form.cleaned_data['filas']
            columnas = form.cleaned_data['columnas']
            
            tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]

    else:
        form = TableroForm()

    return render(request, 'crear_tablero.html', {'form': form, 'tablero': tablero})

def indexer(request):
    return render(request, 'index.html')
