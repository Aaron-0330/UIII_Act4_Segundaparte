# app_uber/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import UsuarioPasajero, Chofer ,Viaje# Importa Chofer también para el ForeignKey
from datetime import date # Para usar en el formulario si no se especifica

def inicio_uber(request):
    return render(request, 'inicio.html')

def agregar_usuario_pasajero(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        genero = request.POST['genero']
        ciudad = request.POST['ciudad']
        chofer_preferido_id = request.POST.get('chofer_preferido') # Puede ser None

        chofer_preferido = None
        if chofer_preferido_id:
            try:
                chofer_preferido = Chofer.objects.get(id_chofer=chofer_preferido_id)
            except Chofer.DoesNotExist:
                pass # Manejar el error si el chofer no existe, o dejarlo en None

        # La fecha de registro se puede establecer automáticamente al crear
        UsuarioPasajero.objects.create(
            nombre=nombre,
            email=email,
            telefono=telefono,
            direccion=direccion,
            fecha_registro=date.today(), # Asignar la fecha actual
            genero=genero,
            ciudad=ciudad,
            chofer_preferido=chofer_preferido
        )
        return redirect('ver_usuario_pasajero')
    
    choferes = Chofer.objects.all() # Para la lista desplegable de choferes
    return render(request, 'usuario_pasajero/agregar_usuario_pasajero.html', {'choferes': choferes})


def ver_usuario_pasajero(request):
    pasajeros = UsuarioPasajero.objects.all()
    return render(request, 'usuario_pasajero/ver_usuario_pasajero.html', {'pasajeros': pasajeros})

def actualizar_usuario_pasajero(request, id_usuario):
    pasajero = get_object_or_404(UsuarioPasajero, pk=id_usuario)
    choferes = Chofer.objects.all() # Para la lista desplegable de choferes
    return render(request, 'usuario_pasajero/actualizar_usuario_pasajero.html', {'pasajero': pasajero, 'choferes': choferes})


def realizar_actualizacion_usuario_pasajero(request, id_usuario):
    if request.method == 'POST':
        pasajero = get_object_or_404(UsuarioPasajero, pk=id_usuario)
        pasajero.nombre = request.POST['nombre']
        pasajero.email = request.POST['email']
        pasajero.telefono = request.POST['telefono']
        pasajero.direccion = request.POST['direccion']
        pasajero.genero = request.POST['genero']
        pasajero.ciudad = request.POST['ciudad']
        
        chofer_preferido_id = request.POST.get('chofer_preferido')
        chofer_preferido = None
        if chofer_preferido_id:
            try:
                chofer_preferido = Chofer.objects.get(id_chofer=chofer_preferido_id)
            except Chofer.DoesNotExist:
                pass
        pasajero.chofer_preferido = chofer_preferido
        
        pasajero.save()
        return redirect('ver_usuario_pasajero')
    return redirect('ver_usuario_pasajero') # Redirigir si no es POST


def borrar_usuario_pasajero(request, id_usuario):
    pasajero = get_object_or_404(UsuarioPasajero, pk=id_usuario)
    if request.method == 'POST':
        pasajero.delete()
        return redirect('ver_usuario_pasajero')
    return render(request, 'usuario_pasajero/borrar_usuario_pasajero.html', {'pasajero': pasajero})
def agregar_chofer(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        licencia = request.POST['licencia']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        email = request.POST['email']
        edad = request.POST['edad']
        fecha_ingreso = request.POST['fecha_ingreso'] # Asume formato YYYY-MM-DD
        
        Chofer.objects.create(
            nombre=nombre,
            licencia=licencia,
            telefono=telefono,
            direccion=direccion,
            email=email,
            edad=edad,
            fecha_ingreso=fecha_ingreso
        )
        return redirect('ver_chofer')
    return render(request, 'chofer/agregar_chofer.html')

def ver_chofer(request):
    choferes = Chofer.objects.all()
    return render(request, 'chofer/ver_chofer.html', {'choferes': choferes})

def actualizar_chofer(request, id_chofer):
    chofer = get_object_or_404(Chofer, pk=id_chofer)
    return render(request, 'chofer/actualizar_chofer.html', {'chofer': chofer})

def realizar_actualizacion_chofer(request, id_chofer):
    if request.method == 'POST':
        chofer = get_object_or_404(Chofer, pk=id_chofer)
        chofer.nombre = request.POST['nombre']
        chofer.licencia = request.POST['licencia']
        chofer.telefono = request.POST['telefono']
        chofer.direccion = request.POST['direccion']
        chofer.email = request.POST['email']
        chofer.edad = request.POST['edad']
        chofer.fecha_ingreso = request.POST['fecha_ingreso']
        chofer.save()
        return redirect('ver_chofer')
    return redirect('ver_chofer') # Redirigir si no es POST

def borrar_chofer(request, id_chofer):
    chofer = get_object_or_404(Chofer, pk=id_chofer)
    if request.method == 'POST':
        chofer.delete()
        return redirect('ver_chofer')
    return render(request, 'chofer/borrar_chofer.html', {'chofer': chofer})
