
function abrirModal() {
    
    window.location.href = "http://127.0.0.1:8000/login/administrador/register/";
    // Abrir el modal
    let myModal = new bootstrap.Modal(document.getElementById('myModal'));
    myModal.show();
}

function abrirModal2() {
    window.location.href = "http://127.0.0.1:8000/administrador/registrar_nomina/";
    // Abrir el modal
    let myModal = new bootstrap.Modal(document.getElementById('myModal'));
    myModal.show();
}

function confirmarEliminar(usuarioId) {
    Swal.fire({
        title: "¿Estás seguro?",
        text: "Una vez eliminado, no podrás recuperar este usuario.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Sí, eliminarlo",
        cancelButtonText: "Cancelar"
    }).then((result) => {
        if (result.isConfirmed) {
            const baseUrl = window.location.origin;
            window.location.href = `${baseUrl}/usuarios/${usuarioId}/eliminar/`;
        }
    });
}



// actualizar usuarios

function mostrarModalActualizar(userId) {
  // Obtener el formulario de actualización mediante una solicitud AJAX
  fetch(`/usuarios/${userId}/actualizar/`)
      .then(response => response.text())
      .then(data => {
          // Mostrar el formulario en el modal
          document.getElementById('formularioActualizacionUsuario').innerHTML = data;
          // Mostrar el modal
          var modal = new bootstrap.Modal(document.getElementById('actualizarUsuarioModal'));
          modal.show();
      });
}




