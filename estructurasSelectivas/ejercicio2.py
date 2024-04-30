#De la linea de la 2 hasta la 3 le decimos al usuario que digite esos datos
CantidadDeZapatillas= int(input("ingrese la cantidad de zapatillas en Unidades, compradas: "))
ValorDecadauna= int(input("ingrese el total a pagar por las zapatillas: "))
# aca multiplicamos la cantidad de zapatillas por el valor de cada una y que imprima el precio a pagar es el resultado de la multiplicacion
subTotal = (CantidadDeZapatillas) * (ValorDecadauna)
print(f"El precio a pagar sin el descuento es del:  {subTotal}")
#aca ponemos que si la cantidad de zapatilas es mayor igual que 3 le haga descuento del 20%
if CantidadDeZapatillas>=3:
    totalaPagar= subTotal-(subTotal*0.20)  
    formatearNumero = str(totalaPagar).split('.')[0]
    print(f"El total a pagar con el descuento del 20% es: {formatearNumero} " )
    #aca ponemos que si la cantidad de zapatilas es menor que 3 le haga descuento del 10% y imprima el total a pagar con el descuento
elif CantidadDeZapatillas<3:
   totalaPagar2 = subTotal-(subTotal*0.10)
   formatearNumero = str(totalaPagar2).split('.')[0]
   print(f"EL Total a pagar con el descuento del 10% es: {formatearNumero} ")