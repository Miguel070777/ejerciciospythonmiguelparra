window.addEventListener("keydown", (e) => {
    if (e.key === "ArrowUp") {
        incremento();
    } else if (e.key === "ArrowDown") {
        decremento();
    }
    else if (e.key === "r"){
        resetear()
    }
});

let contador = 0;
const valor= document.getElementById("valor")

function incremento() {
    contador++;
    document.getElementById("valor").innerText = contador;
}

function decremento() {
    if (contador > 0) {
        contador--;
        document.getElementById("valor").innerText = contador;
    }
}

function resetear() {
    contador = 0;
    document.getElementById("valor").innerText = contador;
}
