var nota1 = parseFloat(prompt("Ingrese la primera nota: "));
var nota2 = parseFloat(prompt("Ingrese la segundo nota: "));
var nota3 = parseFloat(prompt("Ingrese la tercer nota: "));

var promedio = (nota1 + nota2 + nota3) /3;
if(promedio>=0 && promedio<=3.3){
    alert("El promedio es: "+promedio+" No aprobo")
}
    

else if(promedio>=3.4 && promedio<=3.7) {
    alert ("El promedio es: "+promedio+ " plan de mejoramiento")
}

else if(promedio>=3.8 && promedio<=5.0) {
    alert ("El promedio es: "+promedio+ " Aprobó")
}
else{
    alert ("El promedio es: "+promedio+ " verifique sus datos")
}