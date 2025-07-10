from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib import messages
from .models import Platillo, Receta
from .forms import PlatilloForm, RecetaForm


def lista_platillos(request):
    dias_laborales = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
    platillos_por_dia = {}
    for dia in dias_laborales:
        platillos_por_dia[dia] = Platillo.objects.filter(dia_semana=dia).select_related('receta')
    
    return render(request, 'platillos/lista_platillos_semanal.html', {
        'platillos_por_dia': platillos_por_dia,
        'dias_laborales': dias_laborales
    })

def platillo_new(request):
    if request.method == 'POST':
        form = PlatilloForm(request.POST)
        if form.is_valid():
            try:
                platillo = form.save()
                messages.success(request, f'Platillo "{platillo.nombre}" creado exitosamente.')
                return redirect('platillos:lista_platillos')
            except IntegrityError:
                tipo = form.cleaned_data.get('tipo', 'este tipo')
                dia = form.cleaned_data.get('dia_semana', 'este día')
                messages.error(request, f'Ya existe un platillo de tipo "{tipo}" para el día {dia}. No se puede repetir el mismo tipo de platillo en un día. Solo puede haber una Bebida, un Platillo Principal y un Postre por cada día de la semana.')
    else:
        form = PlatilloForm()
    return render(request, 'platillos/crear_editar_platillo.html', {'form': form, 'titulo': 'Nuevo Platillo'})

def platillo_edit(request, pk):
    platillo = get_object_or_404(Platillo, pk=pk)
    if request.method == 'POST':
        form = PlatilloForm(request.POST, instance=platillo)
        if form.is_valid():
            try:
                platillo_actualizado = form.save()
                messages.success(request, f'Platillo "{platillo_actualizado.nombre}" actualizado exitosamente.')
                return redirect('platillos:lista_platillos')
            except IntegrityError:
                tipo = form.cleaned_data.get('tipo', 'este tipo')
                dia = form.cleaned_data.get('dia_semana', 'este día')
                messages.error(request, f'Ya existe un platillo de tipo "{tipo}" para el día {dia}. No se puede repetir el mismo tipo de platillo en un día. Solo puede haber una Bebida, un Platillo Principal y un Postre por cada día de la semana.')
    else:
        form = PlatilloForm(instance=platillo)
    return render(request, 'platillos/crear_editar_platillo.html', {'form': form, 'titulo': 'Editar Platillo'})

def platillo_delete(request, pk):
    platillo = get_object_or_404(Platillo, pk=pk)
    if request.method == 'POST':
        platillo.delete()
        return redirect('platillos:lista_platillos')
    return render(request, 'platillos/confirmar_eliminar_platillo.html', {'platillo': platillo})


def receta_new(request, platillo_pk):
    platillo = get_object_or_404(Platillo, pk=platillo_pk)
    if hasattr(platillo, 'receta'):
        return redirect('platillos:receta_edit', pk=platillo.receta.pk)
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.platillo = platillo
            receta.save()
            return redirect('platillos:lista_platillos')
    else:
        form = RecetaForm()
    return render(request, 'platillos/receta_simple.html', {'form': form, 'titulo': f'Receta para {platillo.nombre}', 'platillo': platillo})

def receta_edit(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == 'POST':
        form = RecetaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('platillos:lista_platillos')
    else:
        form = RecetaForm(instance=receta)
    return render(request, 'platillos/receta_simple.html', {'form': form, 'titulo': f'Editar Receta de {receta.platillo.nombre}', 'platillo': receta.platillo})

def receta_view(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'platillos/receta_detail.html', {'receta': receta})
