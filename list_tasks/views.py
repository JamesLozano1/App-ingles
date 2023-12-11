from django.shortcuts import render, get_object_or_404, redirect
from .models import Materia, Tarea, QuizUsuario, Pregunta, PreguntasRespondidas
from .forms import MateriaForm, TareaForm, CheckBox, RegistroFormulario, UsuarioLoginFormulario
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from rest_framework import viewsets
from .serializer import MateriaSerializer, TareaSerializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist




def loginV(request):
    titulo = 'Ingresar'
    form = UsuarioLoginFormulario(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        usuario = authenticate(username=username, password= password)
        login(request, usuario)
        return redirect('menuQuiz')
    context = {
        'form':form,
        'titulo':titulo,
    }
    return render(request, 'Usuario/login.html', context)

def registro(request):
    titulo = 'Registrar'
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegistroFormulario()
    
    context = {
        'form':form,
        'titulo':titulo,
    }

    return render(request, 'Usuario/registro.html', context)

def logoutV(request):
    logout(request)
    return redirect('inicio')

def tablero(request):
    total_usuarios_quiz = QuizUsuario.objects.order_by('-puntaje_total')[:10]
    contador = total_usuarios_quiz.count()

    context = {
        'usuario_quiz':total_usuarios_quiz,
        'counter_user':contador,
    }

    return render(request, 'play/tablero.html', context)


def jugar(request):
    QuizUser, created = QuizUsuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        respuesta_pk = request.POST.get('respuesta_pk')

        try:
            opcion_seleccionada = pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
        except ObjectDoesNotExist:
            raise Http404

        QuizUser.validar_intentos(pregunta_respondida, opcion_seleccionada)

        return redirect('resultado', pregunta_respondida.pk)
    else:
        pregunta = QuizUser.obtener_nuevas_preguntas() 
        if pregunta is not None:
            QuizUser.crear_intentos(pregunta)

        context = {
            'pregunta': pregunta,
        }
    
    return render(request, 'play/jugar.html', context)

def resultado_pregunta(request, pregunta_respondida_pk):
    respondida = get_object_or_404(PreguntasRespondidas, pk=pregunta_respondida_pk)

    context = {
        'respondida':respondida
    }

    return render(request, 'play/resultados.html', context)

def menuQuiz(request):
    titulo = 'hola'
    context = {
        'titulo':titulo
    }
    return render(request, 'play/menuQ.html', context)



## lo que toca presentar 


def detalle_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)

    if request.method == 'POST':
        form = CheckBox(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
    else:
        form = CheckBox(instance=tarea)

    return render(request, 'componets/detalles.html', {'tarea': tarea, 'form': form})


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializers


def ver_tareas(request):
    tareas = Tarea.objects.all()

    tareas_pasadas = []
    tareas_futuras = []

    now = timezone.now()

    for tarea in tareas:
        if tarea.fecha_vencimiento < now:
            tareas_pasadas.append(tarea)
        else:
            tareas_futuras.append(tarea)

    return render(request, 'componets/ver_tareas.html', {
        'tareas_pasadas': tareas_pasadas,
        'tareas_futuras': tareas_futuras,
        'tareas':tareas,
    })


def Inicio(request):
    titulo = 'Bienvenido'
    return render(request, 'inicio.html', {
        'titulo':titulo
    })

# @login_required
# def ver_tareas(request):
#     tareas = Tarea.objects.all()
#     return render(request, 'componets/ver_tareas.html', {
#         'tareas':tareas,
#     })

# @login_required
def Agregar_Materia(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/AddTarea')
    else:
        form = MateriaForm()
    return render(request, 'componets/Agregar_materia.html', {
        'form':form
    })

# @login_required
def Agregar_Tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TareaForm
    return render(request, 'componets/Agregar_tareas.html', {
        'form':form,
    })

# def exit(request):
#     logout(request)
#     return redirect('inicio')