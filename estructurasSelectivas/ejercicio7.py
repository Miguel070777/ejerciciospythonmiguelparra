#Le pedimos al usuario que digite la cantidad de llantas que desea comprar
cantidadComprada = int(input("Ingrese la cantidad de llantas que desea comprar: ")) 
#Aca, definimos que si la cantidad de compra es igual , menor o mayor cobre segun el precio asignado
if cantidadComprada < 5:
    precio = 300
    totalApagar = cantidadcomprada * precio
elif cantidadComprada<= 10:
    precio = 250
    totalApagar = cantidadComprada * precio
elif cantidadComprada > 10:
    precio = 200
    totalApagar = cantidadComprada * precio


#Aca, es lo que se muestra segun los primeros datos y con la operacion pasada
print(f"El costo por cada llanta es de ${precio}")
print(f"El total a pagar por {cantidadComprada} llantas es de $ {totalApagar}")
