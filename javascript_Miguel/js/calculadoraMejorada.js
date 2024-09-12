function sumar(n1, n2) {
    return n1 + n2;
}

function restar(n1, n2) {
    return n1 - n2;
}

function multiplicar(n1, n2) {
    return n1 * n2;
}

function dividir(n1, n2) {
    return n1 / n2;
}

function potencia(n1, n2) {
    return Math.pow(n1, n2);
}

// Función mostrar con validación de datos
function mostrar() {
    let n1 = parseInt(document.getElementById("n1").value);
    let n2 = parseInt(document.getElementById("n2").value);
    let opc = parseInt(document.getElementById("opc").value);
    let resultado;
    let alerta = document.getElementById("respuesta");
    let resultadoText = document.getElementById("resultado");

    // Validar si los números están presentes
    if (isNaN(n1) || isNaN(n2)) {
        alerta.style.display = "block";
        alerta.classList.remove("alert-warning", "alert-success");
        alerta.classList.add("alert-danger");
        resultadoText.innerHTML = "Verifique sus datos";
        return;
    }

    // Realizar la operación
    switch (opc) {
        case 1:
            resultado = sumar(n1, n2);
            break;
        case 2:
            resultado = restar(n1, n2);
            break;
        case 3:
            resultado = multiplicar(n1, n2);
            break;
        case 4:
            resultado = dividir(n1, n2);
            break;
        case 5:
            resultado = potencia(n1, n2);
            break;
        default:
            resultado = "Opción no válida";
    }

    // Mostrar el resultado
    alerta.style.display = "block";
    alerta.classList.remove("alert-danger", "alert-warning");
    alerta.classList.add("alert-success");
    resultadoText.innerHTML = `El resultado es: ${resultado}`;

}