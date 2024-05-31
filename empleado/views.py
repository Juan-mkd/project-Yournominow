from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from desprendible.models import Devengado, Descuento, Nomina,Valores_fijos
from usuario.models import Usuario, Cargo
from login.views import login_view
from datetime import datetime
from xhtml2pdf import pisa
from django.template.loader import get_template
import io
from django.views import View
from django.utils import timezone
from bs4 import BeautifulSoup
from django.template.loader import render_to_string
from io import BytesIO






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
    valores_fijos = Valores_fijos.objects.first()
    
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
    datos_devengado.total_devengados = total_deveng
    datos_devengado.save()
    
    total_precio = 0
    desc_precios = Descuento.objects.values_list('desc_precio', flat=True)
    
    # contar cuantas bonificaciones hay 
    cantidad_bonificaciones = Devengado.objects.filter(deveng_cedula_id=usuario,deveng_periodo_pago=nomina_periodo_pago, deveng_bonificacion__isnull=False).count()
    
    cant_creditos_libranza = Descuento.objects.filter(desc_cedula_id=usuario, desc_periodo_pago=nomina_periodo_pago, desc_creditos_libranza__isnull=False).count()

    cant_cuotas_sindicales = Descuento.objects.filter(desc_cedula_id=usuario, desc_periodo_pago=nomina_periodo_pago, desc_cuotas_sindicales__isnull=False).count()

    cant_embargos_judiciales = Descuento.objects.filter(desc_cedula_id=usuario, desc_periodo_pago=nomina_periodo_pago, desc_embargos_judiciales__isnull=False).count()

    cant_descuentos = Descuento.objects.filter(desc_cedula_id=usuario, desc_periodo_pago=nomina_periodo_pago, desc_precio__isnull=False).count()

    
    for precio in desc_precios:
        total_precio += precio


    bonificacion = 0
    deveng_bonificacion  = Devengado.objects.values_list('deveng_bonificacion', flat=True)
    
    for bono in deveng_bonificacion:
        bonificacion += bono
        
    
       
    
    
    # Calculos descuentos
    aporte_salud = round(sueldo * valores_fijos.valor_aport_salud)
    aporte_pension = round(sueldo * valores_fijos.valor_aport_pension)
    aporte_sena = round(sueldo *  valores_fijos.valor_aport_sena)
    aporte_icbf = round(sueldo * valores_fijos.valor_aport_icbf)
    total_desc = aporte_salud + aporte_pension + datos_descuento.desc_creditos_libranza + datos_descuento.desc_cuotas_sindicales + datos_descuento.desc_embargos_judiciales + aporte_sena + aporte_icbf
    datos_descuento.total_descuentos = total_desc
    datos_descuento.save()
    total_neto = total_deveng - total_desc
    datos_nomina.total_neto = total_neto
    datos_nomina.save()
    
  
    
    return render(request, "desprendible_nomina.html", {
        'datos_usuario': datos_usuario,
        'datos_cargo': datos_cargo,
        'datos_devengado': datos_devengado,
        'valores_fijos': valores_fijos,
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
        'cantidad_bonificaciones': cantidad_bonificaciones,
        'cant_creditos_libranza': cant_creditos_libranza,
        'cant_cuotas_sindicales': cant_cuotas_sindicales,
        'cant_embargos_judiciales': cant_embargos_judiciales,
        'cant_descuentos': cant_descuentos,
        
    })






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
        html_template = render_to_string(template_path, context)

        # Utilizar BeautifulSoup para eliminar los botones de impresión del PDF del HTML
        soup = BeautifulSoup(html_template, 'html.parser')
        
        
        # se elimina el boton de volver
        volver_button = soup.find('a', {'id': 'volver'})
        if volver_button:
            volver_button.decompose()
        
        
        
        enlace_pdf = soup.find('div', {'id': 'enlace-pdf'})
        if enlace_pdf:
            enlace_pdf.decompose()
        enlace_pdf2 = soup.find('div', {'id': 'enlace-pdf2'})
        if enlace_pdf2:
            enlace_pdf2.decompose()

        html = str(soup)

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
            display: none; /* Ocultar los botones de impresión */
        }

        </style>
        '''
        html = css + html

        # Crear un archivo PDF en memoria
        result = io.BytesIO()

        # Convertir la plantilla HTML en un archivo PDF
        pdf = pisa.CreatePDF(io.BytesIO(html.encode("UTF-8")), dest=result)

        # Verificar si la conversión fue exitosa
        if not pdf.err:
            # Establecer las cabeceras adecuadas para descargar el archivo PDF
            response = HttpResponse(result.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="constancia.pdf"'
            return response

        return HttpResponse('Error al generar el PDF', status=500)










# desprendible de nomina PDF

def generar_pdf(request, nomina_periodo_pago):
    usuario = request.user.cedula
    datos_usuario = get_object_or_404(Usuario, cedula=usuario)
    datos_cargo = get_object_or_404(Cargo, cargo_id=datos_usuario.usu_id_cargo_id)
    valores_fijos = Valores_fijos.objects.first()
    datos_nomina = get_object_or_404(Nomina, nom_cedula_id=usuario, nom_periodo_pago=nomina_periodo_pago)
    datos_devengado = get_object_or_404(Devengado, deveng_cedula_id=usuario, deveng_periodo_pago=nomina_periodo_pago)
    datos_descuento = get_object_or_404(Descuento, desc_cedula_id=usuario, desc_periodo_pago=nomina_periodo_pago)
    
    sueldo = datos_cargo.cargo_sueldo_basico 
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
    aporte_salud = round(sueldo * valores_fijos.valor_aport_salud)
    aporte_pension = round(sueldo * valores_fijos.valor_aport_pension)
    aporte_sena = round(sueldo *  valores_fijos.valor_aport_sena)
    aporte_icbf = round(sueldo * valores_fijos.valor_aport_icbf)
    total_desc = aporte_salud + aporte_pension + datos_descuento.desc_creditos_libranza + datos_descuento.desc_cuotas_sindicales + datos_descuento.desc_embargos_judiciales + aporte_sena + aporte_icbf
    total_neto = total_deveng - total_desc

    # contar cuantas bonificaciones hay 
    cantidad_bonificaciones = Devengado.objects.filter(deveng_cedula_id=usuario,deveng_periodo_pago=nomina_periodo_pago, deveng_bonificacion__isnull=False).count()
    cant_creditos_libranza = Descuento.objects.filter(desc_cedula_id=usuario, desc_periodo_pago=nomina_periodo_pago, desc_creditos_libranza__isnull=False).count()
    cant_cuotas_sindicales = Descuento.objects.filter(desc_cedula_id=usuario, desc_periodo_pago=nomina_periodo_pago, desc_cuotas_sindicales__isnull=False).count()
    cant_embargos_judiciales = Descuento.objects.filter(desc_cedula_id=usuario, desc_periodo_pago=nomina_periodo_pago, desc_embargos_judiciales__isnull=False).count()
    cant_descuentos = Descuento.objects.filter(desc_cedula_id=usuario, desc_periodo_pago=nomina_periodo_pago, desc_precio__isnull=False).count()
    
    bonificacion = 0
    deveng_bonificacion  = Devengado.objects.values_list('deveng_bonificacion', flat=True)

    total_precio = 0
    desc_precios = Descuento.objects.values_list('desc_precio', flat=True)
    for precio in desc_precios:
        total_precio += precio
        
    # Render HTML template
    html_string = render_to_string('desprendible_nomina.html', {
        'datos_usuario': datos_usuario,
        'datos_cargo': datos_cargo,
        'datos_devengado': datos_devengado,
        'valores_fijos': valores_fijos,
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
        'total_precio':total_precio,
        'bonificacion': bonificacion,
        'cantidad_bonificaciones': cantidad_bonificaciones,
        'cant_creditos_libranza': cant_creditos_libranza,
        'cant_cuotas_sindicales': cant_cuotas_sindicales,
        'cant_embargos_judiciales': cant_embargos_judiciales,
        'cant_descuentos': cant_descuentos,
    })

    css = '''
    <style>
    /* Agrega aquí tus estilos CSS */
    /* Por ejemplo: */
    body {
        font-family: "Arial", sans-serif;
        font-size: 12px;
        line-height: 1.6;
    }
    h2{
        text-align: center;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 20px;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 8px;
    }
    th {
        background-color: #f2f2f2;
    }
    /* Agrega más estilos según lo necesites */
    </style>
    '''
    
    html_string = css + html_string
    # Usar BeautifulSoup para eliminar los botones
    soup = BeautifulSoup(html_string, 'html.parser')
    
    # Eliminar el botón de volver
    volver_button = soup.find('a', {'id': 'volver'})
    if volver_button:
        volver_button.decompose()
    
    # Eliminar el botón de descargar
    descargar_button = soup.find('a', {'id': 'descargar-pdf'})
    if descargar_button:
        descargar_button.decompose()

    # Convertir el HTML de nuevo a cadena
    html_string = str(soup)

    # Generar PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="desprendible_nomina.pdf"'
    
    pisa_status = pisa.CreatePDF(
        html_string, dest=response
    )
    
    if pisa_status.err:
        return HttpResponse('Hubo un error al generar el PDF <pre>' + html_string + '</pre>')
    return response


