from django.urls import path
from . import views


urlpatterns = [
    path('login/administrador/register/', views.index, name='register'),
    path('registros/', views.registros, name='registros'),
    path('login/administrador/usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/<int:usu_id>/actualizar/', views.actualizar_usuario, name='actualizar_usuario'),
    path('usuarios/<int:usu_id>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),
    path('usuarios/<int:usu_id>/datos/', views.obtener_datos_usuario, name='obtener_datos_usuario'),
    path("administrador/registrar_nomina/",views.registrar_nomina,name="registrar_nomina"),
    path("procesar_nomina/",views.procesar_nomina,name="procesar_nomina"),
    path("login/administrador/novedades/",views.registrar_novedad,name="registrar_novedad"),
    path("login/administrador/procesar_novedad/",views.procesar_novedad,name="procesar_novedad"),
    path("login/administrador/procesar_descuento/",views.procesar_descuento,name="procesar_descuento"),
    path("login/administrador/informes",views.informes,name="informes"),
    path("login/administrador/alertas",views.alertas,name="alertas"),
]