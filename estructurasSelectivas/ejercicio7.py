#Le pedimos al usuario que digite la cantidad de llantas que desea comprar
cantidad_Comprada = int(input("Ingrese la cantidad de llantas que desea comprar: ")) 
#Aca, definimos que si la cantidad de compra es igual , menor o mayor cobre segun el precio asignado
if cantidad_Comprada < 5:
    precio = 300
    total_A_pagar = cantidad_comprada * precio
elif cantidad_Comprada<= 10:
    precio = 250
    total_A_pagar = cantidad_Comprada * precio
elif cantidad_Comprada > 10:
    precio = 200
    total_A_pagar = cantidad_Comprada * precio


#Aca, es lo que se muestra segun los primeros datos y con la operacion pasada
print(f"El costo por cada llanta es de ${precio}")
print(f"El total a pagar por {cantidad_Comprada} llantas es de $ {total_A_pagar}")