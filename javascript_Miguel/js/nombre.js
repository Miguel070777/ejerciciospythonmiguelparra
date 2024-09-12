var nombre = prompt("Ingrese su nombre: ")
let apellido = prompt("Ingrese su apellido: ")
let añonacimiento=prompt("Ingrese su año de nacimiento")

const fecha = new Date();
const fechaActual=fecha.getFullYear();
let edad=fechaActual-añonacimiento 

if (edad<=5) {
    document.write

document.write("niño "+nombre+ " con apellido  "+apellido+ " tengo: "+edad+" años") 


} else if (edad<=17){
    document.write("joven "+nombre+ " con apellido  "+apellido+ " tengo: "+edad+" años") 

}
else{
    document.write("Señor(a) "+nombre+ " con apellido  "+apellido+ " tengo: "+edad+" años") 

}