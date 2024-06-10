

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




