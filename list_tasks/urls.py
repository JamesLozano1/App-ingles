from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from .views import (
                        MateriaViewSet, 
                        TareaViewSet, 
                        detalle_tarea, 
                        registro, 
                        loginV, 
                        logoutV, 
                        jugar, 
                        resultado_pregunta, 
                        menuQuiz,
                        tablero
                    )

router=routers.DefaultRouter()
router.register(prefix='Materia', basename='Materia', viewset=MateriaViewSet)
router.register(prefix='Tarea', basename='Tarea', viewset=TareaViewSet)

urlpatterns = [
    path('', views.Inicio, name='inicio'),
    path('AddMateria/', views.Agregar_Materia, name='addMateria'),
    path('AddTarea/', views.Agregar_Tarea, name='addTarea'),
    path('tareas/', views.ver_tareas, name='tareas'),
    path('rout/', include(router.urls)),

    path('tareas/<int:tarea_id>/', detalle_tarea, name='detalle_tarea'),


    path('login/', views.loginV, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logoutV, name='logout'),
    # path('logout/', views.exit, name='exit'),

    path('jugar/', views.jugar, name='jugar'),
    path('resultado/<int:pregunta_respondida_pk>/', views.resultado_pregunta, name='resultado'),
    path('menuQ/', views.menuQuiz, name='menuQuiz'),
    path('tablero/', views.tablero, name='tablero')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)