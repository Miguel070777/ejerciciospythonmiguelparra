const contraseña = "hola1234"

let intentos = 3;

for( i = 0;i <intentos; i ++) {
    let contraseñausuario = prompt("Ingrese la contraseña")
    
    if(contraseñausuario === contraseña){
        alert("Bienvenido")
        break;   
    }
    else {
    alert("Contraseña incorrecta, vuelva a intentarlo"+(intentos - i - 1)+" intentos. ");

}
if(i === intentos -1){
    alert(" No tiene mas intentos, no puede acceder ")
}
}


