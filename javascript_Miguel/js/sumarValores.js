var suma = 0;
var continuar = true;

var opcion = prompt("Menú: \n1. Añadir Valores \n2. Mostrar Valores \n3. Salir \n Seleccione Una opcion (1, 2, 3):");

if (opcion =="1"){
    var valor =parseInt(prompt("Introduzca el valor a añadir: "))
    suma +=valor;
    alert("Valor añadido " +valor);
} else if (opcion == "2"){
    alert("La suma actual es: "+suma);

} else if (opcion == "3"){
    alert("Saliendo...");
    continuar = false;
} else {
    alert("Opcion no valida, selecciona 1, 2, 3")
}