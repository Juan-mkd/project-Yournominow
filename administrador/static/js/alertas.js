<<<<<<< HEAD
const notifications = document.querySelector(".notifications"),
buttons = document.querySelectorAll(".buttons .btn");
// Object containing details for different types of toasts
const toastDetails = {
timer: 5000,
success: {
icon: 'fa-circle-check',
text: 'Exito: Nominas generadas exitosamente!.',
},
error: {
icon: 'fa-circle-xmark',
text: 'Error: La fecha de las nominas a generar ya existe.',
},
warning: {
icon: 'fa-triangle-exclamation',
text: 'Warning: This is a warning toast.',
},
info: {
icon: 'fa-circle-info',
text: 'Info: Ingrese la fecha de periodo de pago.',
}
}
const removeToast = (toast) => {
toast.classList.add("hide");
if(toast.timeoutId) clearTimeout(toast.timeoutId); // Clearing the timeout for the toast
setTimeout(() => toast.remove(), 500); // Removing the toast after 500ms
}
const createToast = (id) => {
// Getting the icon and text for the toast based on the id passed
const { icon, text } = toastDetails[id];
const toast = document.createElement("li"); // Creating a new 'li' element for the toast
toast.className = `toast ${id}`; // Setting the classes for the toast
// Setting the inner HTML for the toast
toast.innerHTML = `<div class="column">
                 <i class="fa-solid ${icon}"></i>
                 <span>${text}</span>
              </div>
              <i class="fa-solid fa-xmark" onclick="removeToast(this.parentElement)"></i>`;
notifications.appendChild(toast); // Append the toast to the notification ul
// Setting a timeout to remove the toast after the specified duration
toast.timeoutId = setTimeout(() => removeToast(toast), toastDetails.timer);
}
// Adding a click event listener to each button to create a toast when clicked
buttons.forEach(btn => {
btn.addEventListener("click", () => createToast(btn.id));
=======
document.addEventListener('DOMContentLoaded', function() {
   var form = document.getElementById('registroNomina');
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
                       window.location.href = RegistrarNominaUrl;
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
>>>>>>> version-nicolas
});
