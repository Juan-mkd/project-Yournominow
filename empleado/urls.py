from django.urls import path
from . import views
from .views import ConstanciaLaboralPDFView
from .views import ConstanciaPagadaPDFView
from .views import GenerarPDFView

# from .views import generar_desprendible_nomina_pdf

urlpatterns = [
    path("historial_nomina/",views.index,name="historial_nomina"),
    path("desprendible_nomina/",views.desprendible_nomina,name="desprendible_nomina"),
    path("certificacion/",views.certificacion, name="certificacion"),
    path('constancia_pdf/', ConstanciaLaboralPDFView.as_view(), name='constancia_pdf'),
    path('constancia_pagada_pdf/', ConstanciaPagadaPDFView.as_view(), name='constancia_pagada_pdf'),
    path('generar-pdf/', GenerarPDFView.as_view(), name='generar_pdf'),
   
]