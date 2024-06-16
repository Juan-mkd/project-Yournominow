

// actualizar usuarios

function mostrarModalActualizar(descId) {
    // Obtener el formulario de actualización mediante una solicitud AJAX
    fetch(`/descuentos/${descId}/actualizar/`)
        .then(response => response.text())
        .then(data => {
            // Mostrar el formulario en el modal
            document.getElementById('formularioActualizacionDescuento').innerHTML = data;
            // Mostrar el modal
            var modal = new bootstrap.Modal(document.getElementById('actualizarDescuentoModal'));
            modal.show();
        });
  }