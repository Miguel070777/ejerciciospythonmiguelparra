
let nombre1 = prompt("Ingrese el primer nombre:");
let sueldo1 = parseFloat(prompt("Ingrese el sueldo de " + nombre1 + ":"));

let nombre2 = prompt("Ingrese el segundo nombre:");
let sueldo2 = parseFloat(prompt("Ingrese el sueldo de " + nombre2 + ":"));

if (sueldo1 > sueldo2) {
    alert(nombre1 + " gana más que " + nombre2);
} else if (sueldo2 > sueldo1) {
    alert(nombre2 + " gana más que " + nombre1);
} else {
    alert(nombre1 + " y " + nombre2 + " ganan lo mismo");
}
