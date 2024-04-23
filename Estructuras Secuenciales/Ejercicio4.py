nomVendedor = input("ingrese el nombre del vendedor:" ) # Pedimos que ingrese su nombre el vendedor
sueldo = float(input("ingrese el sueldo")) # pedimos que ingrese el sueldo
#Desde la linea 4 hasta la 5 pedimos que digite las ventas
a = float(input("ingrese la venta 1: ")) 
b = float(input("ingrese la venta 2: "))
c = float(input("ingrese la venta 3: ")) 
comision = (a+b+c) * .10 # "Ingresamos la comisión, toca sumar las 3 variables y multiplicarlas al 10%
#En la linea 9 hasta la 12 pedimos que nos imprima el nombre, sueldo, comision y sueldo total, y con "," concateno
print("El nombre del vendedor es: " , nombre_Vendedor) 
print("El sueldo del vendedor es: ",sueldo) 
print("La comision del mes por las 3 ventas es: ", comision) 
print("El sueldo total con la comision es: ", sueldo+comision ) 