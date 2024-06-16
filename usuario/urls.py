from django.urls import path
from . import views
from django.conf.urls import handler404
from usuario.views import custom_404

handler404 = 'myapp.views.custom_404'


urlpatterns = [

]