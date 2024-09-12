var notasprof= parseInt(prompt("Cuantas Notas Saco el Profesor: "))

var sumanotas =0;
for(i=0 ; i<notasprof ; i++){
    var notaestudiante = parseFloat(prompt("Ingrese su nota #" +i+ ":"))
    sumanotas += notaestudiante;   
}
var promedio = sumanotas/notasprof;
let redondeado = promedio.toFixed(1)

document.write("El promedio de las notas es: "+redondeado)

if(redondeado>0 && redondeado<=3.3){
    document.write("<br> Usted No aprobó")
}
else if(redondeado>3.4 && redondeado<=3.7){
    document.write("<br> Necesita Plan de Mejoramiento")
}
else if(redondeado>3.8 && redondeado<=5.0){
    document.write("<br> Usted aprobó")
}
else{
document.write("Intente de nuevo Verifique sus datos")
}