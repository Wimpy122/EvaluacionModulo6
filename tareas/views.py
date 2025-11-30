from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarea
from .forms import TareaForm



@login_required
def lista_tareas(request):
    tareas = Tarea.objects.filter(user=request.user)
    return render(request, 'lista.html', {'tareas': tareas})

@login_required
def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False) 
            tarea.user = request.user       
            tarea.save()                    
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    
    return render(request, 'agregar.html', {'form': form})

@login_required
def detalle_tarea(request, tarea_id):

    tarea = get_object_or_404(Tarea, id=tarea_id, user=request.user)
    return render(request, 'detalle.html', {'tarea': tarea})

@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, user=request.user)
    tarea.delete() 
    return redirect('lista_tareas')