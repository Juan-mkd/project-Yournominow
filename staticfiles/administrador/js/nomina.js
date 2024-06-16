function generarNomina() {
    var periodoPago = document.getElementById('nomina_periodo_pago').value;
    if (periodoPago === '') {
        // Evitar que el formulario se envíe y la página se recargue
        return;
    } else {
        // cambia el id del boton para la alerta
        document.getElementById('info').id = 'success';
    
        // Agregar un campo oculto al formulario para indicar que se debe procesar la nómina de todos los usuarios
        var input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'procesar_todos';
        input.value = 'true';
        document.getElementById('registroNomina').appendChild(input);

        // Enviar el formulario
        document.getElementById('registroNomina').submit();
    }
}

