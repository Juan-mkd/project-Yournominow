document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('registroForm');
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            var formData = new FormData(form);

            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Mostrar SweetAlert sin botón de confirmación y con temporizador
                    Swal.fire({
                        position: 'center', // Centrar la alerta
                        icon: 'success',
                        title: data.message,
                        showConfirmButton: false,
                        timer: 1500
                    });
                    // Redirigir después de que el SweetAlert se haya mostrado el tiempo del temporizador
                    setTimeout(function() {
                        window.location.href = listarUsuariosUrl;
                    }, 1500);
                } else {
                    Swal.fire({
                        position: 'center', // Centrar la alerta
                        icon: 'error',
                        title: data.message,
                        showConfirmButton: true
                    });
                }
            })
            .catch(error => {
                console.error('Error:', error);
                Swal.fire({
                    position: 'center', // Centrar la alerta
                    icon: 'error',
                    title: 'Ocurrió un error al procesar tu solicitud.',
                    showConfirmButton: true
                });
            });
        });
    }
});



