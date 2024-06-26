from django.urls import path
from . import views
from .views import ConstanciaLaboralPDFView
from .views import ConstanciaPagadaPDFView

from .views import desprendible_nomina, generar_pdf


# from .views import generar_desprendible_nomina_pdf

urlpatterns = [
    path("historial_nomina/",views.historial,name="historial_nomina"),
    # path("desprendible_nomina/",views.desprendible_nomina,name="desprendible_nomina"),
    path("certificacion/",views.certificacion, name="certificacion"),
    path('constancia_pdf/', ConstanciaLaboralPDFView.as_view(), name='constancia_pdf'),
    path('constancia_pagada_pdf/', ConstanciaPagadaPDFView.as_view(), name='constancia_pagada_pdf'),
    path('desprendible_nomina/', desprendible_nomina, name='desprendible_nomina'),
    path('desprendible/pdf/<str:nomina_periodo_pago>/', generar_pdf, name='generar_pdf'),
   
]
