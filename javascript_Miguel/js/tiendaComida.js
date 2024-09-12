// Datos compartidos entre todas las mesas
const items = {
    pizza: { price: 8 },
    hamburguesa: { price: 6 },
    tacos: { price: 5 },
    refresco: { price: 2 },
    cafe: { price: 3 }
};

// Carrito para cada mesa
let cart = {
    mesa1: { pizza: 0, hamburguesa: 0, tacos: 0, refresco: 0, cafe: 0 },
    mesa2: { pizza: 0, hamburguesa: 0, tacos: 0, refresco: 0, cafe: 0 },
    mesa3: { pizza: 0, hamburguesa: 0, tacos: 0, refresco: 0, cafe: 0 },
    mesa4: { pizza: 0, hamburguesa: 0, tacos: 0, refresco: 0, cafe: 0 }
};

function selectTable(tableNumber) {
    // Ocultar todas las mesas
    document.querySelectorAll('.mesa').forEach(mesa => mesa.style.display = 'none');
    
    // Mostrar la mesa seleccionada
    document.getElementById(`mesa${tableNumber}`).style.display = 'block';
}

function toggleMenu(menuId) {
    let menu = document.getElementById(menuId);
    if (menu.style.display === "none" || menu.style.display === "") {
        menu.style.display = "block";
    } else {
        menu.style.display = "none";
    }
}

function changeQuantity(item, amount) {
    const tableNumber = getCurrentTable();
    if (cart[`mesa${tableNumber}`][item] !== undefined) {
        cart[`mesa${tableNumber}`][item] += amount;
        if (cart[`mesa${tableNumber}`][item] < 0) cart[`mesa${tableNumber}`][item] = 0;

        // Actualizar el valor visual en la página
        document.getElementById(`${item}-quantity`).textContent = cart[`mesa${tableNumber}`][item];

        // Actualizar carrito y total
        updateCart(tableNumber);
    } else {
        console.error(`El producto "${item}" no está en el menú.`);
    }
}

function toggleDropdown(mesa) {
    let cartContent = document.getElementById(`cart-${mesa}`);
    if (cartContent.style.display === "none" || cartContent.style.display === "") {
        cartContent.style.display = "block";
    } else {
        cartContent.style.display = "none";
    }
}

function updateCart(mesa) {
    let cartItems = document.getElementById(`cart-items-${mesa}`);
    let itemsInCart = Object.entries(cart[`mesa${mesa}`]).filter(([key, value]) => value > 0);

    if (itemsInCart.length === 0) {
        cartItems.textContent = "Tu carrito está vacío.";
    } else {
        cartItems.innerHTML = itemsInCart.map(([key, value]) => `${key.charAt(0).toUpperCase() + key.slice(1)}: ${value}`).join('<br>');
    }

    updateTotalPrice(mesa);
}

function updateTotalPrice(mesa) {
    let totalPrice = Object.entries(cart[`mesa${mesa}`]).reduce((acc, [key, value]) => acc + (value * items[key].price), 0);
    document.getElementById(`total-price-${mesa}`).textContent = `Total: $${totalPrice.toFixed(2)}`;
}

function getCurrentTable() {
    return Array.from(document.querySelectorAll('.mesa')).findIndex(mesa => mesa.style.display === 'block') + 1;
}