from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView



urlpatterns = [
    path("reset_password/",views.reset_password,name="reset_password"),
    path('login/',views.login_view, name='login'),
    path('recuperar_contraseña/',views.recuperar_contraseña, name='recuperar_contraseña'),
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('login/administrador/', views.administrador, name='administrador'),
    path('login/empleado/', views.empleado, name='empleado'),
    path('',views.home,name='home'),
    path('logout/', views.logout_view1, name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
] 