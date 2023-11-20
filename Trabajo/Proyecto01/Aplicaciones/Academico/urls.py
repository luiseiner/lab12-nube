from django.urls import path
from .import views 

urlpatterns = [
 
    # urls para alumno
    path('',views.home_alumno),
    path('registraralumno',views.registrar_alumno),
    path('eliminaralumno/<codigo_a>',views.eliminar_alumno),
    path('actualizar_alumno/<codigo_a>',views.actualizar_alumno, name='actualizaralumno'),
    path('buscaralumno/', views.buscar_alumno,),
]