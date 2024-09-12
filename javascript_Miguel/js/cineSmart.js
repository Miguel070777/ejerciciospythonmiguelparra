const MAX_CUPOS = 50;
let cuposOcupados = 0;


while (cuposOcupados < MAX_CUPOS) {
    let cantidad = prompt("¿Cuántos cupos quieres ingresar? "+" Cupos Disponibles: "+ (MAX_CUPOS - cuposOcupados)+ " (Número):");

    let cantidadNumerica = +cantidad;


    if (cuposOcupados + cantidadNumerica > MAX_CUPOS) {
        alert("No se pueden ingresar " + cantidadNumerica + " cupos. Solo hay " + (MAX_CUPOS - cuposOcupados) + " cupos disponibles.");
    }
    else {
        cuposOcupados += cantidadNumerica;
        alert("Cupos ocupados: " + cuposOcupados);
        alert("Cupos disponibles: " + (MAX_CUPOS - cuposOcupados));
    }
}

alert("¡El cineSmart está completo!")
