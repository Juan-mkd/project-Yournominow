from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from usuario.models import Usuario,Rol,Cargo
from desprendible.models import Devengado, Nomina,Descuento,Valores_fijos
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def alertas(request):
    return render(request, "administrador/alerts.html")

@login_required
def index(request):
    roles = Rol.objects.all()
    cargos = Cargo.objects.all()
    return render(request, "administrador/register.html", {'roles': roles, 'cargos': cargos})


def registros(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        name = request.POST.get('name')
        correo = request.POST.get('correo')
        telefono = request.POST.get('Telefono')
        adress = request.POST.get('adress')
        password = '123'
        rol_nombre = request.POST.get('usu_rol')
        cargo_nombre = request.POST.get('usu_cargo') 

        # Validar si el correo electrónico ya existe en la base de datos
        if Usuario.objects.filter(usu_correo = correo).exists():
            return JsonResponse({'success': False, 'message': 'El correo electrónico ya está registrado. Por favor, utiliza otro correo.'})
        
        if Usuario.objects.filter(usu_telefono = telefono).exists():
            return JsonResponse({'success': False, 'message': 'El telefono ingresado ya esta registrado'})

    
        try:
            rol = Rol.objects.get(rol_nombre=rol_nombre)
            cargo = Cargo.objects.get(cargo_nombre=cargo_nombre)
        except Rol.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'El rol especificado no existe.'})
        except Cargo.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'El cargo especificado no existe.'})

        # Crear el nuevo usuario con el rol seleccionado
        nuevo_usuario = Usuario(
            cedula=cedula, 
            usu_nombre=name, 
            usu_correo=correo, 
            usu_telefono=telefono, 
            usu_direccion=adress, 
            password=make_password(password), 
            usu_id_rol=rol, 
            usu_id_cargo=cargo
        )
        nuevo_usuario.save()
        # Crear devengado inicial para el usuario
        nuevo_devengado = Devengado(
            deveng_cedula_id=cedula,
            deveng_subs_trans= 0,
            deveng_subs_alim= 0,
            deveng_horas_extra_diur= 0,
            deveng_horas_extra_noct= 0,
            deveng_horas_extra_diur_domfest= 0,
            deveng_horas_extra_noct_domfest= 0,
            deveng_bonificacion= 0,
            deveng_periodo_pago= timezone.now(),
            deveng_fecha= timezone.now(),
            total_devengados=0
        )
        nuevo_devengado.save()
        # Crear descuento inicial para el usuario
        nuevo_descuento = Descuento(
            desc_cedula_id=cedula,
            desc_periodo_pago=timezone.now(),
            desc_creditos_libranza=0,
            desc_cuotas_sindicales=0,
            desc_embargos_judiciales=0,
            desc_precio=0,
            desc_tipo_descuento="fiscal",
            desc_fecha_des=timezone.now(),
            des_time_retardo=0
        )
        nuevo_descuento.save()
        # Crear nomina inicial para el usuario
        nueva_nomina = Nomina(
            nom_cedula_id=cedula,
            nom_fecha_creacion=timezone.now(),
            nom_tipo_pago="Electronico",
            nom_periodo_pago=timezone.now(),
            nom_dias_trabajados=0,
            total_neto=0,
            estado='inicial',
        )
        nueva_nomina.save()


        return JsonResponse({'success': True, 'message': 'Registro exitoso.'})
    
    else:
        return render(request, 'administrador.html')
        
        
        
        
        
        
@login_required(login_url='login/administrador/')
def listar_usuarios(request):
    user_list = Usuario.objects.all()
    page = request.GET.get('page', 1)  # Obtener el número de página desde la URL
    page_size = request.GET.get('pageSize', 5)  # Obtener la cantidad de usuarios por página desde la URL

    paginator = Paginator(user_list, page_size)  # Usar el valor seleccionado por el usuario
    try:
        usuarios = paginator.page(page)
    except PageNotAnInteger:
        usuarios = paginator.page(1)
    except EmptyPage:
        usuarios = paginator.page(paginator.num_pages)

    return render(request, 'administrador/usuarios.html', {'usuarios': usuarios})
 
 
 
 
 
@login_required(login_url='login/administrador/')
def actualizar_usuario(request, usu_id):
    usuario = get_object_or_404(Usuario, usu_id=usu_id)

    if request.method == 'POST':
        nombre = request.POST['name']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        estado = request.POST['estado']
        rol_id = request.POST['rol']
        cargo_id = request.POST['cargo']

        rol = get_object_or_404(Rol, rol_id=rol_id)
        cargo = get_object_or_404(Cargo, cargo_id=cargo_id)
        descuento = get_object_or_404(Descuento, desc_id=usu_id)

        usuario.usu_nombre = nombre
        usuario.usu_correo = correo
        usuario.usu_telefono = telefono
        usuario.usu_direccion = direccion
        usuario.usu_estado = estado
        usuario.usu_id_rol = rol
        usuario.usu_id_cargo = cargo
        usuario.save()

        return redirect('listar_usuarios')

    roles = Rol.objects.all()
    cargos = Cargo.objects.all()
    return render(request, 'administrador/usuarios.html', {'usuario': usuario, 'roles': roles, 'cargos': cargos})

def obtener_datos_actualizar(request, usu_id):
    usuario = Usuario.objects.get(pk=usu_id)
    # Aquí puedes personalizar los datos que deseas enviar al cliente
    data = {
        'cedula': usuario.cedula,
        'nombre': usuario.usu_nombre,
        'correo': usuario.usu_correo,
        'telefono': usuario.usu_telefono,
        'direccion': usuario.usu_direccion,
        'estado': usuario.usu_estado,
        'rol': usuario.usu_id_rol,
        'cargo': usuario.usu_id_cargo,
    }
    return JsonResponse(data)



@login_required(login_url='login/administrador/')
def eliminar_usuario(request, usu_id):  
    usuario = get_object_or_404(Usuario, usu_id=usu_id)
    usuario.delete()
    return redirect('listar_usuarios')


def obtener_datos_usuario(request, usu_id):
    usuario = Usuario.objects.get(pk=usu_id)
    # Aquí puedes personalizar los datos que deseas enviar al cliente
    data = {
        'cedula': usuario.cedula,
        'nombre': usuario.usu_nombre,
        'correo': usuario.usu_correo,
        'telefono': usuario.usu_telefono,
        'direccion': usuario.usu_direccion,
        'estado': usuario.usu_estado,
        'rol': usuario.usu_id_rol,
        'cargo': usuario.usu_id_cargo,
    }
    return JsonResponse(data)



# Nomina ----------------------------------------------------------------------------------------------------



@login_required(login_url='login/administrador/')
def registrar_nomina(request):
    return render(request, "administrador/registrar_nomina.html")




def procesar_nomina(request):
    if request.method == 'POST':
        nomina_periodo_pago = request.POST.get('nomina_periodo_pago')


        if nomina_periodo_pago:
            usuarios = Usuario.objects.all()
            nomina_tipo_pago = 'Electronico'
            dias_trabajados = 30
            nomina_existente = False

            fecha_nomina = datetime.strptime(nomina_periodo_pago, '%Y-%m-%d')
            nomina_year = fecha_nomina.year
            nomina_month = fecha_nomina.month

            if Nomina.objects.filter(nom_periodo_pago=nomina_periodo_pago).exists():
                return JsonResponse({'success': False, 'message': 'La nómina ya existe para esta fecha.'})
            
            for usuario in usuarios:
                cedula = usuario.cedula
                if not cedula:
                    continue  # Saltar si el usuario no tiene cédula
                
                devengado = Devengado.objects.filter(deveng_cedula_id=cedula).first()
                descuento = Descuento.objects.filter(desc_cedula_id=cedula).first()
                nomina = Nomina.objects.filter(nom_cedula_id=cedula).first()

                sueldo_basico_cargo = usuario.usu_id_cargo.cargo_sueldo_basico
                deveng_subs_trans = 0
                deveng_subs_alim = 0
                valores_fijos = Valores_fijos.objects.first()
                # Verificar si el sueldo básico es menor o igual a 2,800,000
                if sueldo_basico_cargo <= 2600000:
                    deveng_subs_trans = valores_fijos.valor_trasporte
                    deveng_subs_alim = valores_fijos.valor_alimentacion

                # Buscar o crear el registro de Devengado para el empleado en la base de datos
                if Devengado.objects.filter(deveng_cedula_id=cedula, deveng_fecha__month=nomina_month, deveng_fecha__year=nomina_year).exists():
                    devengado.deveng_subs_trans = deveng_subs_trans
                    devengado.deveng_subs_alim = deveng_subs_alim
                    devengado.deveng_periodo_pago = nomina_periodo_pago
                    devengado.save()
                else:
                    # Crear devengado inicial para el usuario
                    devengado = Devengado(
                        deveng_cedula_id=cedula,
                        deveng_subs_trans= deveng_subs_trans,
                        deveng_subs_alim= 0,
                        deveng_horas_extra_diur= 0,
                        deveng_horas_extra_noct= 0,
                        deveng_horas_extra_diur_domfest= 0,
                        deveng_horas_extra_noct_domfest= 0,
                        deveng_bonificacion= 0,
                        deveng_periodo_pago= nomina_periodo_pago,
                        deveng_fecha= timezone.now(),
                        total_devengados=0
                    )
                    devengado.save()


                if Descuento.objects.filter(desc_cedula_id=cedula, desc_fecha_des__month=nomina_month, desc_fecha_des__year=nomina_year, desc_tipo_descuento='fiscal').exists():
                    descuento.desc_periodo_pago = nomina_periodo_pago
                    descuento.save()
                else:
                    # Crear descuento inicial para el usuario
                    descuento = Descuento(
                        desc_cedula_id=cedula,
                        desc_periodo_pago=nomina_periodo_pago,
                        desc_creditos_libranza=0,
                        desc_cuotas_sindicales=0,
                        desc_embargos_judiciales=0,
                        desc_precio=0,
                        desc_tipo_descuento="fiscal",
                        desc_fecha_des=timezone.now(),
                        des_time_retardo=0
                    )
                    descuento.save()

                if Nomina.objects.filter(nom_cedula_id=cedula, estado='pendiente').exists():
                    return JsonResponse({'success': False, 'message': 'Nominas de algunos empleados pendientes por pagar.'})
                elif Nomina.objects.filter(nom_cedula_id=cedula, estado='inicial').exists():
                    nomina = get_object_or_404(Nomina, nom_cedula_id=cedula, estado='inicial')
                    nomina.delete()  
                    # Crear o actualizar Nomina
                    nomina = Nomina(
                        nom_cedula_id=cedula,
                        nom_fecha_creacion=timezone.now(),
                        nom_tipo_pago="Electronico",
                        nom_periodo_pago=nomina_periodo_pago,
                        nom_dias_trabajados=0,
                        total_neto=0,
                        estado='pagado',
                    )
                    nomina.save()
                elif Nomina.objects.filter(nom_cedula_id=cedula, estado='pagado').exists():
                                        # Crear o actualizar Nomina
                    nomina = Nomina(
                        nom_cedula_id=cedula,
                        nom_fecha_creacion=timezone.now(),
                        nom_tipo_pago="Electronico",
                        nom_periodo_pago=nomina_periodo_pago,
                        nom_dias_trabajados=0,
                        total_neto=0,
                        estado='pendiente',
                    )
                    nomina.save()


                # Calcular devengados
                horas_diurnas = round(sueldo_basico_cargo / 235)
                tot_horas_extra_diurnas = horas_diurnas * devengado.deveng_horas_extra_diur * 0.25
                tot_horas_extra_nocturnas = horas_diurnas * devengado.deveng_horas_extra_noct * 0.75
                tot_horas_extra_diur_domfest = horas_diurnas * devengado.deveng_horas_extra_diur_domfest * 1
                tot_horas_extra_noct_domfest = horas_diurnas * devengado.deveng_horas_extra_noct_domfest * 1.5

                horas_extra_diurnas = horas_diurnas * devengado.deveng_horas_extra_diur + round(tot_horas_extra_diurnas)
                horas_extra_nocturnas = horas_diurnas * devengado.deveng_horas_extra_noct + round(tot_horas_extra_nocturnas)
                horas_extra_diur_domfest = horas_diurnas * devengado.deveng_horas_extra_diur_domfest + round(tot_horas_extra_diur_domfest)
                horas_extra_noct_domfest = horas_diurnas * devengado.deveng_horas_extra_noct_domfest + round(tot_horas_extra_noct_domfest)

                total_deveng = sueldo_basico_cargo + devengado.deveng_subs_trans + devengado.deveng_subs_alim + horas_extra_diurnas + horas_extra_nocturnas + horas_extra_diur_domfest + horas_extra_noct_domfest + devengado.deveng_bonificacion
                devengado.total_devengados = total_deveng
                devengado.save()

                # Calcular descuentos
                aporte_salud = round(sueldo_basico_cargo * valores_fijos.valor_aport_salud)
                aporte_pension = round(sueldo_basico_cargo * valores_fijos.valor_aport_pension)
                aporte_sena = round(sueldo_basico_cargo * valores_fijos.valor_aport_sena)
                aporte_icbf = round(sueldo_basico_cargo * valores_fijos.valor_aport_icbf)

                total_desc = aporte_salud + aporte_pension + descuento.desc_creditos_libranza + descuento.desc_cuotas_sindicales + descuento.desc_embargos_judiciales + aporte_sena + aporte_icbf
                descuento.total_descuentos = total_desc
                descuento.save()

                # Calcular total neto
                total_neto = total_deveng - total_desc
                nomina.total_neto = total_neto
                nomina.save()
            return JsonResponse({'success': True, 'message': 'Registro exitoso.'})
                

        return render(request, 'registrar_nomina.html', {'nomina_existente': nomina_existente})

    return render(request, 'administrador/registrar_nomina.html')


def obtener_datos_nomina(request, nom_id):
    nomina = Nomina.objects.get(pk=nom_id)
    # Aquí puedes personalizar los datos que deseas enviar al cliente
    data = {
        'cedula': nomina.nom_cedula,
        'fecha_creacion': nomina.nom_fecha_creacion,
        'tipo_pago': nomina.nom_tipo_pago,
        'periodo_pago': nomina.nom_periodo_pago,
        'dias_trabajados': nomina.nom_dias_trabajados,
    }
    return JsonResponse(data)


# Novedades ----------------------------------------------------------------------------------------------

@never_cache
@login_required(login_url='login/administrador/')

def procesar_novedad(request):
    if request.method == 'POST':
        # Se obtienen los datos para ingresar en la DB
        cedula = request.POST.get('cedula')
        fecha_reporte = request.POST.get('fecha_reporte')
        horaDiur = int(request.POST.get('horaDiur', 0))
        horaNoct = int(request.POST.get('horaNoct', 0))
        horaDiurDomfest = int(request.POST.get('horaDiurDomfest', 0))
        horaNoctDomfest = int(request.POST.get('horaNoctDomfest', 0))
        bonificacion = int(request.POST.get('deveng_bonificacion', 0))
        fecha_creado = datetime.now()

        fecha_nomina = datetime.strptime(fecha_reporte, '%Y-%m-%d')
        nomina_year = fecha_nomina.year
        nomina_month = fecha_nomina.month
        
        # Define valores por defecto para deveng_subs_trans y deveng_subs_alim
        deveng_subs_trans = 0
        deveng_subs_alim = 0

        # Verificar si ya existe un registro con la misma cédula
        if Devengado.objects.filter(deveng_cedula_id=cedula, deveng_fecha__year=nomina_year, deveng_fecha__month=nomina_month).exists():
            # Obtener el registro existente      
            devengado = get_object_or_404(Devengado, deveng_cedula_id=cedula, deveng_fecha__year=nomina_year, deveng_fecha__month=nomina_month)
            devengado.deveng_horas_extra_diur += horaDiur
            devengado.deveng_horas_extra_noct += horaNoct
            devengado.deveng_horas_extra_diur_domfest += horaDiurDomfest
            devengado.deveng_horas_extra_noct_domfest += horaNoctDomfest
            devengado.deveng_bonificacion += bonificacion
        else:
            # Se crea un nuevo objeto Devengado con los valores proporcionados
            devengado = Devengado(
                deveng_cedula_id=cedula,
                deveng_periodo_pago=fecha_reporte,
                deveng_horas_extra_diur=horaDiur,
                deveng_horas_extra_noct=horaNoct,
                deveng_horas_extra_diur_domfest=horaDiurDomfest,
                deveng_horas_extra_noct_domfest=horaNoctDomfest,
                deveng_bonificacion=bonificacion,
                deveng_subs_trans=deveng_subs_trans,
                deveng_subs_alim=deveng_subs_alim,
                deveng_fecha=fecha_creado,
            )
        # Se guarda el objeto Devengado en la base de datos
        devengado.save()

        # Devolver una respuesta JSON indicando el éxito del registro
        return JsonResponse({'success': True, 'message': 'Registro devengado exitoso!!'})
    
    
def procesar_descuento(request):
    if request.method == 'POST':
        # Datos que ingresan a la DB
        cedula = request.POST.get('cedula')
        fecha_periodo_pago = request.POST.get('nomina_periodo')
        creditos_libranza = int(request.POST.get('creditos_libranza', 0))
        cuotas_sindicales = int(request.POST.get('cuotas_sindicales', 0))
        embargos_judiciales = int(request.POST.get('embargos_judiciales', 0))
        descuento_tipo = request.POST.get('descuento_tipo')
        precio = int(request.POST.get('precio', 0))
        retardos = int(request.POST.get('cantidad_retardo', 0))  # Convertir a entero
        fecha = datetime.now()

        fecha_nomina = datetime.strptime(fecha_periodo_pago, '%Y-%m-%d')
        nomina_year = fecha_nomina.year
        nomina_month = fecha_nomina.month
        
        # Multiplicar retardos por 1000 para obtener el tiempo de retardo en pesos
        des_time_retardo = retardos * 5531
        if Descuento.objects.filter(desc_cedula_id=cedula, desc_fecha_des__year=nomina_year, desc_fecha_des__month=nomina_month, desc_tipo_descuento="fiscal").exists():
            descuento = get_object_or_404(Descuento, desc_cedula_id=cedula, desc_fecha_des__year=nomina_year, desc_fecha_des__month=nomina_month, desc_tipo_descuento="fiscal")
            descuento.desc_periodo_pago = fecha_periodo_pago
            descuento.desc_creditos_libranza = creditos_libranza
            descuento.desc_cuotas_sindicales = cuotas_sindicales
            descuento.desc_embargos_judiciales = embargos_judiciales
        else:
            # Crear un nuevo objeto Descuento con los valores proporcionados
            descuento = Descuento(
                desc_cedula_id=cedula,
                desc_periodo_pago=fecha_periodo_pago,
                desc_creditos_libranza=creditos_libranza,
                desc_cuotas_sindicales=cuotas_sindicales,
                desc_embargos_judiciales=embargos_judiciales,
                desc_precio=precio,
                desc_tipo_descuento="fiscal",
                desc_fecha_des=fecha,
                des_time_retardo=des_time_retardo
            )
        # Guardar el nuevo objeto Descuento en la base de datos
        descuento.save()
            
        # Devolver una respuesta JSON indicando el éxito del registro
        return JsonResponse({'success': True, 'message': 'Registro descuento exitoso !!.'})

def procesar_retardo(request):
    cedula = request.POST.get('cedula')
    fecha_reporte = request.POST.get('fecha_reporte')
    descuentoUsuario = Descuento.objects.filter(desc_cedula_id=cedula).order_by('-desc_periodo_pago').first()
    fecha_desprendible = descuentoUsuario.desc_periodo_pago
    if isinstance(fecha_desprendible, str):
        # Si 'desc_periodo_pago_mas_reciente' ya es una cadena, no necesitas convertirla
        fecha_desprendible = datetime.strptime(fecha_desprendible, "%Y-%m-%d").date()
    mensaje = request.POST.get('mensaje')
    horas_retardo = int(request.POST.get('horas_retardo', 0))
    fecha = datetime.now()

    fecha_nomina = datetime.strptime(fecha_reporte, '%Y-%m-%d')
    nomina_year = fecha_nomina.year
    nomina_month = fecha_nomina.month

    # Multiplicar retardos por 1000 para obtener el tiempo de retardo en pesos
    des_time_retardo = horas_retardo * 5531
    if Descuento.objects.filter(desc_cedula_id=cedula, desc_fecha_des__year=nomina_year, desc_fecha_des__month=nomina_month, desc_tipo_descuento="retardo").exists():
        descuento = get_object_or_404(Descuento, desc_cedula_id=cedula, desc_fecha_des__year=nomina_year, desc_fecha_des__month=nomina_month, desc_tipo_descuento="retardo")
        descuento.des_time_retardo += horas_retardo
    else:
        # Se crea un nuevo objeto Devengado con los valores proporcionados
        descuento = Descuento(
            desc_cedula_id=cedula,
            desc_periodo_pago=fecha_reporte,
            desc_creditos_libranza=0,
            desc_cuotas_sindicales=0,
            desc_embargos_judiciales=0,
            desc_precio=0,
            desc_tipo_descuento= "retardo",
            des_time_retardo=horas_retardo,  
            desc_fecha_des=fecha        
        )
        # Se guarda el objeto Devengado en la base de datos
    descuento.save()
    return JsonResponse({'success': True, 'message': 'Registro de retardo exitoso !!.'})

@login_required(login_url='login/administrador/')
def registrar_novedad(request):
    return render (request, "administrador/novedades.html")

def obtener_datos_novedad(request, deveng_id):
    devengado = Devengado.objects.get(pk=deveng_id)
    # Aquí puedes personalizar los datos que deseas enviar al cliente
    data = {
        'fecha_reporte': devengado.deveng_periodo_pago,
        'horas_diur': devengado.deveng_horas_extra_diur,
        'horas_noct': devengado.deveng_horas_extra_noct,
        'horas_diur_domfest': devengado.deveng_horas_extra_diur_domfest,
        'horas_noct_domfest': devengado.deveng_horas_extra_noct_domfest,
        'bonificacion': devengado.deveng_bonificacion,
    }
    return JsonResponse(data)

def edicion_novedades(request):
    deveng_list = Devengado.objects.all()
    page = request.GET.get('page', 1)  # Obtener el número de página desde la URL
    page_size = request.GET.get('pageSize', 5)  # Obtener la cantidad de usuarios por página desde la URL

def edicion_novedades(request):
    deveng_list = Devengado.objects.all()
    page = request.GET.get('page', 1)  # Obtener el número de página desde la URL
    page_size = request.GET.get('pageSize', 5)  # Obtener la cantidad de usuarios por página desde la URL
    paginator = Paginator(deveng_list, page_size)  # Usar el valor seleccionado por el usuario
    try:
        devengados = paginator.page(page)
    except PageNotAnInteger:
        devengados = paginator.page(1)
    except EmptyPage:
        devengados = paginator.page(paginator.num_pages)
    return render (request, 'administrador/edicion_novedades.html', {'devengados': devengados})

def actualizar_novedad(request, deveng_id):
    devengado = get_object_or_404(Devengado, deveng_id=deveng_id)

    if request.method == 'POST':
        # fecha_reporte = request.POST['fecha']
        hora_extra_diur = request.POST['hora_extra_diur']
        hora_extra_noct = request.POST['hora_extra_noct']
        hora_extra_diur_domfest = request.POST['hora_extra_diur_domfest']
        hora_extra_noct_domfest = request.POST['hora_extra_noct_domfest']
        bonificaciones = request.POST['bonificaciones']

        # devengado.deveng_periodo_pago = fecha_reporte
        devengado.deveng_horas_extra_diur = hora_extra_diur
        devengado.deveng_horas_extra_noct = hora_extra_noct
        devengado.deveng_horas_extra_diur_domfest = hora_extra_diur_domfest
        devengado.deveng_horas_extra_noct_domfest = hora_extra_noct_domfest
        devengado.deveng_bonificacion = bonificaciones

        devengado.save()

        return redirect('edicion_novedades')

    return render(request, 'administrador/edicion_novedades.html', {'devengado': devengado})

def edicion_descuentos(request):
    desc_list = Descuento.objects.all()
    page = request.GET.get('page', 1)  # Obtener el número de página desde la URL
    page_size = request.GET.get('pageSize', 5)  # Obtener la cantidad de usuarios por página desde la URL
    paginator = Paginator(desc_list, page_size)  # Usar el valor seleccionado por el usuario
    try:
        descuentos = paginator.page(page)
    except PageNotAnInteger:
        descuentos = paginator.page(1)
    except EmptyPage:
        descuentos = paginator.page(paginator.num_pages)
    return render (request, 'administrador/edicion_descuentos.html', {'descuentos': descuentos})

def actualizar_descuentos(request, desc_id):
    descuento = get_object_or_404(Descuento, desc_id=desc_id)

    if request.method == 'POST':
        # fecha_reporte = request.POST['fecha']
        desc_creditos_libranza = request.POST['desc_creditos_libranza']
        desc_cuotas_sindicales = request.POST['desc_cuotas_sindicales']
        desc_embargos_judiciales = request.POST['desc_embargos_judiciales']

        # descuento.desc_periodo_pago = fecha_reporte
        descuento.desc_creditos_libranza = desc_creditos_libranza
        descuento.desc_cuotas_sindicales = desc_cuotas_sindicales
        descuento.desc_embargos_judiciales = desc_embargos_judiciales
        descuento.save()

        return redirect('edicion_descuentos')

    return render(request, 'administrador/edicion_descuentos.html', {'descuento': descuento})

def obtener_datos_novedad(request, deveng_id):
    devengado = Devengado.objects.get(pk=deveng_id)
    # Aquí puedes personalizar los datos que deseas enviar al cliente
    data = {
        'fecha_reporte': devengado.deveng_periodo_pago,
        'horas_diur': devengado.deveng_horas_extra_diur,
        'horas_noct': devengado.deveng_horas_extra_noct,
        'horas_diur_domfest': devengado.deveng_horas_extra_diur_domfest,
        'horas_noct_domfest': devengado.deveng_horas_extra_noct_domfest,
        'bonificacion': devengado.deveng_bonificacion,
    }
    return JsonResponse(data)

def obtener_datos_descuento(request, desc_id):
    descuento = Descuento.objects.get(pk=desc_id)
    # Aquí puedes personalizar los datos que deseas enviar al cliente
    data = {
        'fecha_reporte': descuento.desc_fecha_des,
        'creditos_libranza': descuento.desc_creditos_libranza,
        'cuotas_sindicales': descuento.desc_cuotas_sindicales,
        'emabrgos_judiciales': descuento.desc_emabrgos_judiciales,
    }
    return JsonResponse(data)


# informess ----------------------------------------------------------------------------------------------


def informes(request):
    usuarios = Usuario.objects.all()
    cargos = Cargo.objects.all()
    total_usuarios = Usuario.objects.count()
    total_nominas = Nomina.objects.count()
    descuentos = Descuento.objects.all()
    valores_fijos = Valores_fijos.objects.first()  # Obtener los valores fijos (solo necesitas uno)
    fiscal = 'fiscal'

    

    nominas = Nomina.objects.select_related('nom_cedula', 'nom_cedula__usu_id_cargo').all()
    devengados = Devengado.objects.select_related('deveng_cedula').all()

    # Calcular el total de netos a pagar solo para las nóminas pendientes
    total_neto_a_pagar = sum(nomina.total_neto for nomina in nominas if nomina.estado == 'pendiente')

    context = {
        'fiscal': fiscal,
        'total_usuarios': total_usuarios,
        'usuarios': usuarios,
        'cargos': cargos,
        'descuentos': descuentos,
        'valores_fijos': valores_fijos,
        'nominas': nominas,
        'devengados': devengados,
        'total_nominas': total_nominas,
        'total_neto_a_pagar': total_neto_a_pagar,
    }

    return render(request, "administrador/informes.html", context)







@csrf_exempt
def pagar_nomina(request):
    if request.method == 'POST':
        # Actualizar todas las nóminas en una sola operación
        Nomina.objects.all().update(estado='pagado')
        
        # Redireccionar a la página de informes o a donde desees
        return redirect('informes')  

    return render(request, 'administrador/informes.html')


def eliminar_devengado(request, devengado_id):
    devengado = get_object_or_404(Devengado, pk=devengado_id)

    if request.method == 'POST':
        # Verificar si el método de solicitud es POST (a través de un formulario o AJAX)

        try:
            devengado.delete()  # Eliminar el objeto Devengado de la base de datos
            messages.success(request, 'El devengado ha sido eliminado correctamente.')
        except Exception as e:
            messages.error(request, f'Hubo un problema al intentar eliminar el devengado: {str(e)}')

        return redirect('edicion_novedades')  # Redireccionar a la página de edición de novedades

    return redirect('edicion_novedades')  



def eliminar_descuento(request, descuento_id):
    descuento = get_object_or_404(Descuento, pk=descuento_id)

    if request.method == 'POST':
        try:
            descuento.delete()
            messages.success(request, 'El descuento ha sido eliminado correctamente.')
        except Exception as e:
            messages.error(request, f'Hubo un problema al intentar eliminar el descuento: {str(e)}')

        return redirect('edicion_descuentos')

    return redirect('edicion_descuentos')
