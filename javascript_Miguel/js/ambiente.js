let ocupados4102 = 0;
let ocupados2108 = 0;
const limite4102 = 25;
const limite2108 = 30;

while (true) {
    let opcion = prompt(
        "Elige una opción:\n" +
        "1. Ambiente 4102 (Ocupados: " + ocupados4102 + " / " + limite4102 + ")\n" +
        "2. Ambiente 2108 (Ocupados: " + ocupados2108 + " / " + limite2108 + ")\n" +
        "3. Salir"
    );

    opcion = parseInt(opcion);

    switch(opcion) {
        case 1:
            let personas4102 = prompt("¿Cuántas personas deseas agregar al Ambiente 4102? (Máximo " + (limite4102 - ocupados4102) + ")");
            personas4102 = parseInt(personas4102);

            if (personas4102 > 0 && ocupados4102 + personas4102 <= limite4102) {
                ocupados4102 += personas4102;
                alert("Has asignado " + personas4102 + " personas al Ambiente 4102. Ocupados: " + ocupados4102 + " / " + limite4102);
            } else {
                alert("Número de personas no válido o excede el límite disponible.");
            }
            break;

        case 2:
            let personas2108 = prompt("¿Cuántas personas deseas agregar al Ambiente 2108? (Máximo " + (limite2108 - ocupados2108) + ")");
            personas2108 = parseInt(personas2108);

            if (personas2108 > 0 && ocupados2108 + personas2108 <= limite2108) {
                ocupados2108 += personas2108;
                alert("Has asignado " + personas2108 + " personas al Ambiente 2108. Ocupados: " + ocupados2108 + " / " + limite2108);
            } else {
                alert("Número de personas no válido o excede el límite disponible.");
            }
            break;

        case 3:
            alert("Saliendo del sistema...");
            break;

        default:
            alert("Opción no válida. Por favor, elige 1, 2 o 3.");
            break;
    }

    if (opcion === 3) {
        break;
    }
}
