from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TareaForm
from django.http import Http404

# Create your views here.

TAREAS_DB = []

def get_next_id():
    if not TAREAS_DB:
        return 1
    return TAREAS_DB[-1]['id'] + 1

@login_required
def lista_tareas(request):
    mis_tareas = [t for t in TAREAS_DB if t['user_id'] == request.user.id]
    return render(request, 'lista.html', {'tareas': mis_tareas})

@login_required
def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            nueva_tarea = {
                'id': get_next_id(),
                'titulo': form.cleaned_data['titulo'],
                'descripcion': form.cleaned_data['descripcion'],
                'user_id': request.user.id
            }
            TAREAS_DB.append(nueva_tarea)
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    
    return render(request, 'agregar.html', {'form': form})

@login_required
def detalle_tarea(request, tarea_id):
    tarea = next((t for t in TAREAS_DB if t['id'] == tarea_id and t['user_id'] == request.user.id), None)
    
    if not tarea:
        raise Http404("Tarea no encontrada o no tienes permisos")
        
    return render(request, 'detalle.html', {'tarea': tarea})

@login_required
def eliminar_tarea(request, tarea_id):
    tarea = next((t for t in TAREAS_DB if t['id'] == tarea_id and t['user_id'] == request.user.id), None)
    
    if tarea:
        TAREAS_DB.remove(tarea)
    
    return redirect('lista_tareas')