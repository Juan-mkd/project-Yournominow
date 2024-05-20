
// En tu archivo JavaScript (por ejemplo, alerts.js)

// Obtiene el botón y le añade un evento click
document.getElementById("activar-alerta").addEventListener("click", function() {
    // Utiliza SweetAlert para mostrar una alerta
    Swal.fire({
      title: "Do you want to save the changes?",
      showDenyButton: true,
      showCancelButton: true,
      confirmButtonText: "Save",
      denyButtonText: `Don't save`
    }).then((result) => {
      /* Read more about isConfirmed, isDenied below */
      if (result.isConfirmed) {
        Swal.fire("Saved!", "", "success");
      } else if (result.isDenied) {
        Swal.fire("Changes are not saved", "", "info");
      }
    });
});
