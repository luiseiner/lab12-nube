from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Alumno
from django.core.files.storage import default_storage
from django.conf import settings

def home_alumno(request):
    alumnos = Alumno.objects.order_by('codigo_a')
    return render(request, 'GestionAlumno.html', {"alumno": alumnos})

def registrar_alumno(request):
    if request.method == 'POST':
        codigo_a = request.POST["txtcodigo"]
        apellido = request.POST["txtapellido"]
        nombre = request.POST["txtnombre"]
        correo = request.POST["correo"]
        fecha_nac = request.POST["fecha"]
        
        foto = request.FILES.get('foto')
        
        alumno = Alumno(codigo_a=codigo_a, apellido=apellido, nombre=nombre, correo=correo, fecha_nac=fecha_nac)
        
        if foto:
              # Definir la ruta en S3 donde se guardará la imagen
            mybucketslab12 = f'imagenes/{codigo_a}_{foto.name}'

            # Guardar la imagen en S3
            file_path = default_storage.save(mybucketslab12, foto)

            # Obtener la URL de la imagen en S3
            image_url = default_storage.url(file_path)
             # Guardar la imagen en S3
            

            # Obtener la URL de la imagen en S3
            image_url = f"{settings.AWS_STORAGE_BUCKET_NAME}/{file_path}"

            # Guardar el alumno con la URL de la imagen en S3
            alumno = Alumno(
                codigo_a=codigo_a,
                apellido=apellido,
                nombre=nombre,
                correo=correo,
                fecha_nac=fecha_nac,
                foto=image_url
            )
        
        alumno.save()
        
        alumnos = Alumno.objects.order_by('codigo_a')
        return render(request, 'GestionAlumno.html', {"alumno": alumnos})
    else:
        return render(request, '/')

def eliminar_alumno(request, codigo_a):
    alumno = Alumno.objects.get(codigo_a=codigo_a)
    alumno.delete()
    alumnos = Alumno.objects.order_by('codigo_a')
    return render(request, 'GestionAlumno.html', {"alumno": alumnos})

def actualizar_alumno(request, codigo_a):
    alumno = Alumno.objects.get(codigo_a=codigo_a)
    
    if request.method == 'POST':
        apellido = request.POST.get("txtapellido")
        nombre = request.POST.get("txtnombre")
        fecha_nac = request.POST.get("fecha")
        correo = request.POST.get("correo")
        
        # Verifica si se subió una nueva imagen
        nueva_imagen = request.FILES.get('nueva_imagen')
        
        # Actualiza los datos del alumno
        alumno.apellido = apellido
        alumno.nombre = nombre
        alumno.fecha_nac = fecha_nac
        alumno.correo = correo
        
        # Si hay una nueva imagen, actualiza la imagen del alumno
        if nueva_imagen:
            alumno.imagen = nueva_imagen
        
        # Guarda los cambios en el alumno
        alumno.save()
        
        alumnos = Alumno.objects.order_by('codigo_a')
        return render(request, 'GestionAlumno.html', {"alumno": alumnos})
    else:
        return render(request, 'formulario_actualizacion.html', {'alumno': alumno})
def buscar_alumno(request):
    if request.method == 'GET':
        nombre = request.GET.get('txtnombre')
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
        return render(request, 'GestionAlumno.html', {'alumno': alumnos})
    return HttpResponse("Método no permitido")
