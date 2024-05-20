from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from desprendible.models import Devengado, Descuento, Nomina
from usuario.models import Usuario, Cargo
from login.views import login_view
from datetime import datetime
from xhtml2pdf import pisa
from django.template.loader import get_template
import io
from django.views import View
from django.utils import timezone
from bs4 import BeautifulSoup



def index(request):
    usuario=request.user.cedula
    fechas= Nomina.objects.filter(nom_cedula_id=usuario)
    for nomina in fechas:
        nomina.nom_periodo_pago = nomina.nom_periodo_pago.strftime("%Y-%m-%d")
    return render(request,'historial_nomina.html',{'fechas':fechas})



# Create your views here.
def desprendible_nomina(request):
    usuario = request.user.cedula
    if request.method == 'POST':
        nomina_periodo_pago = request.POST.get('nomina_periodo_pago')
       
    # Aquí se trae información importante para acceder a los datos del desprendible
    usuario = request.user.cedula
    datos_usuario = Usuario.objects.get(cedula=usuario)
    
    datos_cargo = Cargo.objects.get(cargo_id=datos_usuario.usu_id_cargo_id)  # Obtener cargo del usuario
    sueldo = datos_cargo.cargo_sueldo_basico  # Obtener sueldo según el cargo
    
    
    
    datos_nomina = Nomina.objects.get(nom_cedula_id=usuario, nom_periodo_pago=nomina_periodo_pago)
    datos_devengado = Devengado.objects.filter(deveng_cedula_id=usuario, deveng_periodo_pago=nomina_periodo_pago).first()
    datos_descuento = Descuento.objects.filter(desc_cedula_id=usuario, desc_periodo_pago=nomina_periodo_pago).first()
    
  
        
        
        
    # Calculos devengados
    horas_diurnas = round(sueldo / 235) 
    tot_horas_extra_diurnas = horas_diurnas * datos_devengado.deveng_horas_extra_diur * 0.25
    tot_horas_extra_nocturnas = horas_diurnas * datos_devengado.deveng_horas_extra_noct * 0.75
    tot_horas_extra_diur_domfest = horas_diurnas * datos_devengado.deveng_horas_extra_diur_domfest * 1
    tot_horas_extra_noct_domfest = horas_diurnas * datos_devengado.deveng_horas_extra_noct_domfest * 1.5
    horas_extra_diurnas = horas_diurnas * datos_devengado.deveng_horas_extra_diur + round(tot_horas_extra_diurnas)
    horas_extra_nocturnas = horas_diurnas * datos_devengado.deveng_horas_extra_noct + round(tot_horas_extra_nocturnas)
    horas_extra_diur_domfest = horas_diurnas * datos_devengado.deveng_horas_extra_diur_domfest + round(tot_horas_extra_diur_domfest)
    horas_extra_noct_domfest = horas_diurnas * datos_devengado.deveng_horas_extra_noct_domfest + round(tot_horas_extra_noct_domfest)    
    total_deveng = sueldo + datos_devengado.deveng_subs_trans + datos_devengado.deveng_subs_alim + horas_extra_diurnas + horas_extra_nocturnas + horas_extra_diur_domfest + horas_extra_noct_domfest + datos_devengado.deveng_bonificacion
    
    
    total_precio = 0
    desc_precios = Descuento.objects.values_list('desc_precio', flat=True)
    
    for precio in desc_precios:
        total_precio += precio


    bonificacion = 0
    deveng_bonificacion  = Devengado.objects.values_list('deveng_bonificacion', flat=True)
    
    for bono in deveng_bonificacion:
        bonificacion += bono
        
    
       
    
    
    # Calculos descuentos
    aporte_salud = round(sueldo * 0.04)
    aporte_pension = round(sueldo * 0.04)
    aporte_sena = round(sueldo * 0.04)
    aporte_icbf = round(sueldo * 0.04)
    total_desc = aporte_salud + aporte_pension + datos_descuento.desc_creditos_libranza + datos_descuento.desc_cuotas_sindicales + datos_descuento.desc_embargos_judiciales + aporte_sena + aporte_icbf
    total_neto = total_deveng - total_desc
    
    return render(request, "desprendible_nomina.html", {
        'datos_usuario': datos_usuario,
        'datos_cargo': datos_cargo,
        'datos_devengado': datos_devengado,
        'datos_nomina': datos_nomina,
        'datos_descuento': datos_descuento,
        'total_deveng': total_deveng,
        'horas_extra_diurnas': horas_extra_diurnas,
        'horas_extra_nocturnas': horas_extra_nocturnas,
        'horas_extra_diur_domfest': horas_extra_diur_domfest,
        'horas_extra_noct_domfest': horas_extra_noct_domfest,
        'aporte_salud': aporte_salud,
        'aporte_pension': aporte_pension,
        'aporte_sena': aporte_sena,
        'aporte_icbf': aporte_icbf,
        'total_desc': total_desc,
        'total_neto': total_neto,
        'total_precio': total_precio,
        'bonificacion': bonificacion,
    })

def certificacionSueldo(request):
    # Recuperar el usuario autenticado
    usuario = request.user
    fecha_actual = timezone.now().strftime("%d/%m/%Y")
    # Pasar los datos del usuario a la plantilla
    context = {
        'usuario': usuario,
        'fecha_actual': fecha_actual,
    }

    return render(request, "certificacionSueldo.html", context)



def certificacion(request):
    # Recuperar el usuario autenticado
    usuario = request.user
    fecha_actual = timezone.now().strftime("%d/%m/%Y")
    # Pasar los datos del usuario a la plantilla
    context = {
        'usuario': usuario,
        'fecha_actual': fecha_actual,
    }

    return render(request, "certificacion.html", context)

class ConstanciaPagadaPDFView(View):
    def get(self, request):
        # Obtener el usuario (ajustar esto según tus necesidades)
        usuario = Usuario.objects.first()
        # Obtener la fecha actual
        fecha_actual = timezone.now().strftime("%d/%m/%Y")
        # Renderizar la plantilla HTML con el contexto

        template_path = 'certificacionSueldo.html'

        context = {
            'usuario': usuario,
            'fecha_actual': fecha_actual,
        }
        template = get_template(template_path)
        html = template.render(context)

        # Agregar los estilos CSS al HTML
        css = '''
        <style>
        /* Agrega aquí tus estilos CSS */
        /* Por ejemplo: */
        body {
            font-family: "Arial", sans-serif;
            font-size: 16px;
            line-height: 1.6;
        }

        .container {
            margin: 50px auto;
            max-width: 600px;
            padding: 20px;
        }

        .logo {
            text-align: center;
            margin-bottom: 20px;
        }

        h1 {
            text-align: center;
            font-size: 24px;
            margin-bottom: 30px;
        }

        .info {
            margin-bottom: 20px;
        }

        .info p {
            margin-bottom: 10px;
        }

        .footer {
            margin-top: 30px;
            text-align: left;
        }

        .btn-certificacion {
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }

        .btn-certificacion button {
            padding: 10px 20px;
            background-color: #333;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .btn-certificacion button:hover {
            background-color: #222;
        }

        </style>
        '''
        html = css + html

        # Utilizar BeautifulSoup para eliminar el enlace del PDF del HTML
        soup = BeautifulSoup(html, 'html.parser')
        enlace_pdf = soup.find('div', {'id': 'enlace-pdf'})
        if enlace_pdf:
            enlace_pdf.decompose()
        html = str(soup)

        # Crear un archivo PDF en memoria
        result = io.BytesIO()

        # Convertir la plantilla HTML en un archivo PDF
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)

        # Verificar si la conversión fue exitosa
        if not pdf.err:
            # Establecer las cabeceras adecuadas para descargar el archivo PDF
            response = HttpResponse(result.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="constancia.pdf"'
            return response

        return HttpResponse('Error al generar el PDF', status=500)

class ConstanciaLaboralPDFView(View):
    def get(self, request):
        # Obtener el usuario (ajustar esto según tus necesidades)
        usuario = Usuario.objects.first()
        # Obtener la fecha actual
        fecha_actual = timezone.now().strftime("%d/%m/%Y")
        # Renderizar la plantilla HTML con el contexto

        template_path = 'certificacion.html'

        context = {
            'usuario': usuario,
            'fecha_actual': fecha_actual,
        }
        template = get_template(template_path)
        html = template.render(context)

        # Agregar los estilos CSS al HTML
        css = '''
        <style>
        /* Agrega aquí tus estilos CSS */
        /* Por ejemplo: */
        body {
            font-family: "Arial", sans-serif;
            font-size: 16px;
            line-height: 1.6;
        }

        .container {
            margin: 50px auto;
            max-width: 600px;
            padding: 20px;
        }

        .logo {
            text-align: center;
            margin-bottom: 20px;
        }

        h1 {
            text-align: center;
            font-size: 24px;
            margin-bottom: 30px;
        }

        .info {
            margin-bottom: 20px;
        }

        .info p {
            margin-bottom: 10px;
        }

        .footer {
            margin-top: 30px;
            text-align: left;
        }

        .btn-certificacion {
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }

        .btn-certificacion button {
            padding: 10px 20px;
            background-color: #333;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .btn-certificacion button:hover {
            background-color: #222;
        }

        </style>
        '''
        html = css + html

        # Utilizar BeautifulSoup para eliminar el enlace del PDF del HTML
        soup = BeautifulSoup(html, 'html.parser')
        enlace_pdf = soup.find('div', {'id': 'enlace-pdf'})
        if enlace_pdf:
            enlace_pdf.decompose()
        html = str(soup)

        enlace_pdf2 = soup.find('div', {'id': 'enlace-pdf2'})
        if enlace_pdf2:
            enlace_pdf2.decompose()

        # Crear un archivo PDF en memoria
        result = io.BytesIO()

        # Convertir la plantilla HTML en un archivo PDF
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)

        # Verificar si la conversión fue exitosa
        if not pdf.err:
            # Establecer las cabeceras adecuadas para descargar el archivo PDF
            response = HttpResponse(result.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="constancia.pdf"'
            return response

        return HttpResponse('Error al generar el PDF', status=500)




class DesprendibleNominaPDFView(View):
    def get(self, request):
        usuario = request.user
        nomina_periodo_pago = request.POST.get('nomina_periodo_pago')

        datos_usuario = {
            'usu_nombre': usuario.usu_nombre, 
            'cedula': usuario.cedula,
            'usu_correo': usuario.usu_correo,
            'usu_fecha_ingreso': usuario.usu_fecha_ingreso.strftime("%d/%m/%Y"),  # Asegúrate de que la fecha esté en el formato correcto
        }
        datos_cargo = {
            'cargo_nombre': usuario.usu_id_cargo.cargo_nombre,  
            'cargo_empresa': usuario.usu_id_cargo.cargo_empresa,
            'cargo_sueldo_basico': usuario.usu_id_cargo.cargo_sueldo_basico,
        }
        datos_nomina = {
            'nom_periodo_pago': nomina_periodo_pago,
            'nom_dias_trabajados': 30,  # Puedes ajustar esto según lo que obtengas de tus modelos de datos
        }
        datos_devengado = {
            'deveng_subs_trans': 100,  # Puedes ajustar esto según lo que obtengas de tus modelos de datos
            'deveng_subs_alim': 50,  # Puedes ajustar esto según lo que obtengas de tus modelos de datos
            'deveng_horas_extra_diur': 10,  # Puedes ajustar esto según lo que obtengas de tus modelos de datos
            'deveng_horas_extra_noct': 20,  # Puedes ajustar esto según lo que obtengas de tus modelos de datos
            'deveng_horas_extra_diur_domfest': 5,  # Puedes ajustar esto según lo que obtengas de tus modelos de datos
            'deveng_horas_extra_noct_domfest': 10,  # Puedes ajustar esto según lo que obtengas de tus modelos de datos
            'deveng_bonificacion': 200,  # Puedes ajustar esto según lo que obtengas de tus modelos de datos
        }
        total_deveng = 1500  # Puedes ajustar esto según los cálculos que realices

        # Calcular los valores de los descuentos
        sueldo = datos_cargo['cargo_sueldo_basico']
        aporte_salud = round(sueldo * 0.04)
        aporte_pension = round(sueldo * 0.04)
        aporte_sena = round(sueldo * 0.04)
        aporte_icbf = round(sueldo * 0.04)
        total_desc = aporte_salud + aporte_pension + aporte_sena + aporte_icbf

        # Calcular el sueldo neto
        total_neto = total_deveng - total_desc

        # Renderizar la plantilla HTML con los datos
        template_path = 'desprendible_nomina.html'
        context = {
            'datos_usuario': datos_usuario,
            'datos_cargo': datos_cargo,
            'datos_nomina': datos_nomina,
            'datos_devengado': datos_devengado,
            'total_deveng': total_deveng,
            'aporte_salud': aporte_salud,
            'aporte_pension': aporte_pension,
            'aporte_sena': aporte_sena,
            'aporte_icbf': aporte_icbf,
            'total_desc': total_desc,
            'total_neto': total_neto,
        }
        template = get_template(template_path)
        html = template.render(context)

        # Eliminar el enlace PDF del HTML
        soup = BeautifulSoup(html, 'html.parser')
        enlace_pdf = soup.find('div', {'id': 'enlace-pdf'})
        if enlace_pdf:
            enlace_pdf.decompose()
        html = str(soup)

        # Crear un archivo PDF en memoria
        result = io.BytesIO()

        # Convertir el template HTML en un archivo PDF
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)

        # Verificar si la conversión fue exitosa
        if not pdf.err:
            # Establecer las cabeceras adecuadas para descargar el archivo PDF
            response = HttpResponse(result.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="desprendible_nomina.pdf"'
            return response

        return HttpResponse('Error al generar el PDF', status=500)
