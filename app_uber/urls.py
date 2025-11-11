# app_uber/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_uber, name='inicio_uber'),
    path('usuario_pasajero/agregar/', views.agregar_usuario_pasajero, name='agregar_usuario_pasajero'),
    path('usuario_pasajero/ver/', views.ver_usuario_pasajero, name='ver_usuario_pasajero'),
    path('usuario_pasajero/actualizar/<int:id_usuario>/', views.actualizar_usuario_pasajero, name='actualizar_usuario_pasajero'),
    path('usuario_pasajero/actualizar/realizar/<int:id_usuario>/', views.realizar_actualizacion_usuario_pasajero, name='realizar_actualizacion_usuario_pasajero'),
    path('usuario_pasajero/borrar/<int:id_usuario>/', views.borrar_usuario_pasajero, name='borrar_usuario_pasajero'),

     # URLs para Choferes (NUEVAS)
    path('chofer/agregar/', views.agregar_chofer, name='agregar_chofer'),
    path('chofer/ver/', views.ver_chofer, name='ver_chofer'),
    path('chofer/actualizar/<int:id_chofer>/', views.actualizar_chofer, name='actualizar_chofer'),
    path('chofer/actualizar/realizar/<int:id_chofer>/', views.realizar_actualizacion_chofer, name='realizar_actualizacion_chofer'),
    path('chofer/borrar/<int:id_chofer>/', views.borrar_chofer, name='borrar_chofer'),
    
   
]