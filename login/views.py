from django.shortcuts import render,HttpResponse,redirect,redirect,get_object_or_404
from  usuario.models import Usuario,Rol
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import logout,authenticate, login
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import rotate_token
from django.views.decorators.cache import never_cache
from yournominow import settings
from django.views import View
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.decorators import login_required
from django.contrib import messages





def home(request):
    return render(request,"index.html")



def recuperar_contraseña(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        try:
            usuario = Usuario.objects.get(usu_correo=correo)
        except Usuario.DoesNotExist:
            return render(request, 'recuperar_contraseña.html', {'mensaje': 'El correo electrónico proporcionado no está asociado a ninguna cuenta.'})

        token = default_token_generator.make_token(usuario)
        uid = urlsafe_base64_encode(force_bytes(usuario.pk))
        reset_link = request.build_absolute_uri('/reset_password/{}/{}/'.format(uid, token))
        correo_html = render_to_string('email/reset_password_email.html', {'reset_link': reset_link})

        # Enviar el correo electrónico utilizando las configuraciones de settings.py
        send_mail(
            'Forgot Password',
            '',
            settings.DEFAULT_FROM_EMAIL,
            [correo],
            html_message=correo_html
        )

        return render(request, 'recuperar_contraseña.html', {'mensaje': 'Se ha enviado un correo electrónico con instrucciones para restablecer tu contraseña.'})
    else:
        return render(request, 'recuperar_contraseña.html', {})
 



def reset_password(request, uidb64, token):

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Usuario.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Usuario.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            # Obtener la nueva contraseña del formulario
            new_password = request.POST['new_password']
            
            # Actualizar la contraseña del usuario en la base de datos
            user.password = make_password(new_password)  # Hash de la nueva contraseña
            user.save()
            
            # Redirigir al usuario a la página de inicio de sesión
            return redirect("login")  # Cambia 'login' por el nombre de tu vista de inicio de sesión
        else:
            return render(request, 'reset_password.html', {'uidb64': uidb64, 'token': token})
    else:
        return render(request, 'reset_password_invalid.html')
    






@never_cache   

def login_view(request):
    # Verificar si hay una sesión activa y cerrarla
    if request.user.is_authenticated:
        logout(request)
    
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        password = request.POST.get('password')
        usuario = authenticate(request, cedula=cedula, password=password)
        
        if usuario is not None:
            if usuario.usu_estado == 'activo':
                login(request, usuario)
                rotate_token(request)
            
                if usuario.usu_id_rol_id == 1:  
                    return redirect("administrador")
                elif usuario.usu_id_rol_id == 2:  
                    return redirect("empleado")
            else:
                mensaje_error = "El usuario está inactivo."
                return render(request, 'login.html', {'mensaje_error': mensaje_error})
        
        # Autenticación fallida
        if usuario is None:
            
            mensaje_error = "Cédula o contraseña incorrecta."
            return render(request, 'login.html', {'mensaje_error': mensaje_error})
    
    # Redirigir al inicio de sesión
    return render(request, 'login.html')




@never_cache
@csrf_protect
@login_required(login_url='login/administrador/')
def administrador(request):
    if request.user.is_authenticated and request.user.usu_id_rol_id == 1:
        user = request.user
        usuarios = Usuario.objects.filter(usu_nombre=user.usu_nombre)
        usuario = usuarios.first()
        if request.method == 'POST':
            foto = request.FILES.get('foto')
            usuario.image = foto
            usuario.save()
            print(usuario.image)
        request.session['context'] = 'administrador'  # Establece el contexto en la sesión
        context = {'usuario': usuario}
        return render(request, "administrador.html", context)
    
    return redirect(settings.LOGIN_REDIRECT_URL)


@never_cache
@login_required(login_url='login/empleado')
def empleado(request):
    if request.user.is_authenticated and request.user.usu_id_rol_id == 2:
        user = request.user
        empleado = Usuario.objects.get(cedula=user.cedula)
        request.session['context'] = 'empleado'  # Establece el contexto en la sesión
        context = {'usuario': empleado}
        return render(request, "empleado.html", context)
    
    return redirect(settings.LOGIN_REDIRECT_URL)




    
@never_cache
def logout_view1(request):
    logout(request) 
    response = HttpResponse()
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return redirect(settings.LOGIN_REDIRECT_URL)
  
  




@login_required
def perfil_usuario(request):
    usuario = request.user
    rol = request.user.usu_id_rol.rol_nombre
    # Pasar los datos del usuario a la plantilla
 
    
    if request.method == 'POST':
        if 'submit_perfil' in request.POST:
            # Procesar los datos del formulario de perfil
            nuevo_nombre = request.POST.get('usu_nombre')
            nuevo_correo = request.POST.get('usu_correo')
            nuevo_telefono = request.POST.get('usu_telefono')
            nueva_direccion = request.POST.get('usu_direccion')

            usuario.usu_nombre = nuevo_nombre
            usuario.usu_correo = nuevo_correo
            usuario.usu_telefono = nuevo_telefono
            usuario.usu_direccion = nueva_direccion

            usuario.save()
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('perfil_usuario')
        elif 'submit_contraseña' in request.POST:
            # Procesar los datos del formulario de cambio de contraseña
            contraseña_actual = request.POST.get('contraseña_actual')
            nueva_contraseña = request.POST.get('nueva_contraseña')
            confirmar_contraseña = request.POST.get('confirmar_contraseña')

            # Verificar la contraseña actual
            if check_password(contraseña_actual, usuario.password):
                if nueva_contraseña == confirmar_contraseña:
                    usuario.password = make_password(nueva_contraseña)
                    usuario.save()
                    messages.success(request, 'Contraseña cambiada exitosamente.')
                    return redirect('perfil_usuario')
                else:
                    messages.error(request, 'Las contraseñas no coinciden.')
            else:
                messages.error(request, 'La contraseña actual es incorrecta.')

    return render(request, 'editar_usuario.html', {'usuario': usuario, 'rol': rol})






@login_required
def mi_vista(request):
    # Obtener el usuario actual
    usuario = request.user
    # Obtener el nombre de usuario desde el modelo Usuario
    usuario_model = Usuario.objects.get(user=usuario)
    nombre_usuario = usuario_model.usu_nombre
    # Pasar el nombre de usuario a la plantilla en el contexto
    return render(request, 'navbarAdministrador.html', {'nombre_usuario': nombre_usuario})
