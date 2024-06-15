

// actualizar usuarios

function mostrarModalActualizar(devengId) {
  // Obtener el formulario de actualización mediante una solicitud AJAX
  fetch(`/devengados/${devengId}/actualizar/`)
      .then(response => response.text())
      .then(data => {
          // Mostrar el formulario en el modal
          document.getElementById('formularioActualizacionDevengado').innerHTML = data;
          // Mostrar el modal
          var modal = new bootstrap.Modal(document.getElementById('actualizarDevengadoModal'));
          modal.show();
      });
}



// devengado.js
function confirmarEliminar(devengadoId) {
    Swal.fire({
        title: '¿Estás seguro?',
        text: "Esta acción no se puede revertir. ¿Deseas eliminar este devengado?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            // Si el usuario confirma la eliminación, enviar el formulario
            document.getElementById(`formEliminarDevengado${devengadoId}`).submit();
        }
    });
}