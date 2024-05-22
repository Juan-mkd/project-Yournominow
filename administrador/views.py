from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from usuario.models import Usuario,Rol,Cargo
from desprendible.models import Devengado, Nomina,Descuento
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

# Create your views here.

def alertas(request):
    return render(request, "alerts.html")

@login_required
def index(request):
    roles = Rol.objects.all()
    cargos = Cargo.objects.all()
    return render(request, "register.html", {'roles': roles, 'cargos': cargos})



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

    return render(request, 'usuarios.html', {'usuarios': usuarios})
 
 
 
 
 
@login_required(login_url='login/administrador/')
def actualizar_usuario(request, usu_id):
    usuario = get_object_or_404(Usuario, usu_id=usu_id)

    if request.method == 'POST':
        cedula = request.POST['cedula']
        nombre = request.POST['name']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        estado = request.POST['estado']
        rol_id = request.POST['rol']
        cargo_id = request.POST['cargo']

        rol = get_object_or_404(Rol, rol_id=rol_id)
        cargo = get_object_or_404(Cargo, cargo_id=cargo_id)

        usuario.cedula = cedula
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
    return render(request, 'usuarios.html', {'usuario': usuario, 'roles': roles, 'cargos': cargos})





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
    return render(request, "registrar_nomina.html")

def procesar_nomina(request):
    if request.method == 'POST':
        # Obtener el periodo de pago del formulario
        nomina_periodo_pago = request.POST.get('nomina_periodo_pago')

        # Verificar si se proporcionó un periodo de pago
        if nomina_periodo_pago:
            # Obtener todos los usuarios
            usuarios = Usuario.objects.all()

            # Definir el tipo de pago de la nómina y los días trabajados
            nomina_tipo_pago = 'Electronico'
            dias_trabajados = 30

            # Variable para verificar si hay una nómina existente para este periodo
            nomina_existente = False

            # Iterar sobre todos los usuarios y generar la nómina para cada uno
            for usuario in usuarios:
                cedula = usuario.cedula

                # Obtener el sueldo básico del cargo asociado al usuario
                sueldo_basico_cargo = usuario.usu_id_cargo.cargo_sueldo_basico

                # Definir los subsidios de transporte y alimentación según el sueldo básico
                if sueldo_basico_cargo <= 2800000:
                    deveng_subs_trans = 150000
                    deveng_subs_alim = 60000
                else:
                    deveng_subs_trans = 0
                    deveng_subs_alim = 0

                # Verificar si ya existe una nómina para este usuario en este período
                if Nomina.objects.filter(nom_periodo_pago=nomina_periodo_pago, nom_cedula_id=cedula).exists():
                    nomina_existente = True
            
                else:
         
                    # Obtener los datos de devengados para el usuario
                    devengados = Devengado.objects.filter(deveng_cedula_id=cedula, deveng_periodo_pago=nomina_periodo_pago)

                    # Obtener los datos de descuentos para el usuario
                    descuentos = Descuento.objects.filter(desc_cedula_id=cedula, desc_periodo_pago=nomina_periodo_pago)

                    # Obtener los valores de los devengados y descuentos
                    deveng_horas_extra_diur = devengados.values_list('deveng_horas_extra_diur', flat=True).first() or 0
                    deveng_horas_extra_noct = devengados.values_list('deveng_horas_extra_noct', flat=True).first() or 0
                    deveng_horas_extra_diur_domfest = devengados.values_list('deveng_horas_extra_diur_domfest', flat=True).first() or 0
                    deveng_horas_extra_noct_domfest = devengados.values_list('deveng_horas_extra_noct_domfest', flat=True).first() or 0
                    deveng_bonificacion = devengados.values_list('deveng_bonificacion', flat=True).first() or 0

                    desc_creditos_libranza = descuentos.values_list('desc_creditos_libranza', flat=True).first() or 0
                    desc_cuotas_sindicales = descuentos.values_list('desc_cuotas_sindicales', flat=True).first() or 0
                    desc_embargos_judiciales = descuentos.values_list('desc_embargos_judiciales', flat=True).first() or 0
                    des_time_retardo = descuentos.values_list('des_time_retardo', flat=True).first() or 0
                    desc_precio = descuentos.values_list('desc_precio', flat=True).first() or 0

                    # Crear y guardar el devengado y la nómina para el usuario
                    nuevo_devengado = Devengado(
                        deveng_cedula_id=cedula,
                        deveng_subs_trans=deveng_subs_trans,
                        deveng_subs_alim=deveng_subs_alim,
                        deveng_horas_extra_diur=deveng_horas_extra_diur,
                        deveng_horas_extra_noct=deveng_horas_extra_noct,
                        deveng_horas_extra_diur_domfest=deveng_horas_extra_diur_domfest,
                        deveng_horas_extra_noct_domfest=deveng_horas_extra_noct_domfest,
                        deveng_bonificacion=deveng_bonificacion,
                        deveng_periodo_pago=nomina_periodo_pago,
                        deveng_fecha=datetime.now())
                    nuevo_devengado.save()

                    nuevo_descuento = Descuento(
                        desc_cedula_id=cedula,
                        desc_creditos_libranza=desc_creditos_libranza,
                        desc_cuotas_sindicales=desc_cuotas_sindicales,
                        desc_embargos_judiciales=desc_embargos_judiciales,
                        desc_periodo_pago=nomina_periodo_pago,
                        desc_fecha_des=datetime.now(),
                        des_time_retardo=des_time_retardo,
                        desc_precio =  desc_precio,
                    )
                    nuevo_descuento.save()

                    nueva_nomina = Nomina(
                        nom_cedula_id=cedula,
                        nom_fecha_creacion=datetime.now(),
                        nom_tipo_pago=nomina_tipo_pago,
                        nom_periodo_pago=nomina_periodo_pago,
                        nom_dias_trabajados=dias_trabajados)
                    nueva_nomina.save()

            # Renderizar la página con la indicación de si la nómina existía o no
            return render(request, 'registrar_nomina.html', {'nomina_existente': nomina_existente})

    # Si no se envió un formulario POST o faltan datos, redirigir a la página de registro de nómina
    return render(request, 'registrar_nomina.html')




@never_cache
@login_required(login_url='login/administrador/')

def procesar_novedad(request):
    if request.method == 'POST':
        # Se obtienen los datos para ingresar en la DB
        cedula = request.POST.get('cedula')
        fecha_periodo = request.POST.get('nomina_periodo')
        horaDiur = int(request.POST.get('horaDiur', 0))
        horaNoct = int(request.POST.get('horaNoct', 0))
        horaDiurDomfest = int(request.POST.get('horaDiurDomfest', 0))
        horaNoctDomfest = int(request.POST.get('horaNoctDomfest', 0))
        bonificacion = int(request.POST.get('deveng_bonificacion', 0))
        fecha_creado = datetime.now()
       
        
        # Define valores por defecto para deveng_subs_trans y deveng_subs_alim
        deveng_subs_trans = 0
        deveng_subs_alim = 0

        # Verificar si ya existe un registro con la misma cédula
        if Devengado.objects.filter(deveng_cedula_id=cedula, deveng_periodo_pago=fecha_periodo).exists():
            # Obtener el registro existente      
            devengado = get_object_or_404(Devengado, deveng_cedula_id=cedula, deveng_periodo_pago=fecha_periodo)
            devengado.deveng_horas_extra_diur += horaDiur
            devengado.deveng_horas_extra_noct += horaNoct
            devengado.deveng_horas_extra_diur_domfest += horaDiurDomfest
            devengado.deveng_horas_extra_noct_domfest += horaNoctDomfest
            devengado.deveng_bonificacion += bonificacion
        else:
            # Se crea un nuevo objeto Devengado con los valores proporcionados
            devengado = Devengado(
                deveng_cedula_id=cedula,
                deveng_periodo_pago=fecha_periodo,
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
        return JsonResponse({'success': True, 'message': 'Registro exitoso!!'})
    
    
    




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
        
        # Multiplicar retardos por 1000 para obtener el tiempo de retardo en pesos
        des_time_retardo = retardos * 5531
        
        # Crear un nuevo objeto Descuento con los valores proporcionados
        descuento = Descuento(
            desc_cedula_id=cedula,
            desc_periodo_pago=fecha_periodo_pago,
            desc_creditos_libranza=creditos_libranza,
            desc_cuotas_sindicales=cuotas_sindicales,
            desc_embargos_judiciales=embargos_judiciales,
            desc_precio=precio,
            desc_tipo_descuento=descuento_tipo,
            desc_fecha_des=fecha,
            des_time_retardo=des_time_retardo
        )
        
        # Guardar el nuevo objeto Descuento en la base de datos
        descuento.save()
        
        # Devolver una respuesta JSON indicando el éxito del registro
        return JsonResponse({'success': True, 'message': 'Registro exitoso !!.'})










def obtener_datos_nomina(request, nom_id):
    nomina = Nomina.objects.get(pk=nom_id)
    # Aquí puedes personalizar los datos que deseas enviar al cliente
    dataNomi = {
        'cedula': nomina.nom_cedula_id,
        'fecha_creacion': nomina.nom_fecha_creacion,
        'tipo_pago': nomina.nom_tipo_pago,
        'periodo_pago': nomina.nom_periodo_pago,
        'dias_trabajados': nomina.nom_dias_trabajados,
    }
    return JsonResponse(dataNomi)




@login_required(login_url='login/administrador/')
def registrar_novedad(request):
    return render (request, "novedades.html")















# informess ----------------------------------------------------------------------------------------------
def informes(request):
    usuarios = Usuario.objects.all()
    cargos = Cargo.objects.all()
    total_usuarios = Usuario.objects.count()
    
    context = {
        'total_usuarios': total_usuarios,
        'usuarios': usuarios,
        'cargos': cargos,
    }
    
    return render(request, "informes.html", context)