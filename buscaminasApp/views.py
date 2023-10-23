from django.shortcuts import render
from .forms import TableroForm

def crea_tablero(request):
    tablero = None

    if request.method == 'POST':
        form = TableroForm(request.POST)
        if form.is_valid():
            filas = form.cleaned_data['filas']
            columnas = form.cleaned_data['columnas']
            
            tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]

    else:
        form = TableroForm()

    return render(request, 'crea_tablero.html', {'form': form, 'tablero': tablero})

