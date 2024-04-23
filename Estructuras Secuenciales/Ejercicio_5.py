valorCompra=int(input("Digite el valor de la compra : "))
descuento=int(input("Digite el descuento : "))
'''Primero declare las variables y puse el comando int para indicarle al input que son numeros enteros y le pido al usuario con el input que me proporcione la informacion'''
sacarDescuento=descuento / 100 
#segundo, hacemos la operacion de dividir el descuento sobre 100 que es 100% del valor del descuento
multiplicar=sacarDescuento * valorCompra
#tercero, multiplique el descuento por el valor de la compra para saber cuanto se le va restar al precio final
precioFinal=valorCompra - multiplicar
#cuarto, aca se coge el valor de la compra y se le resta el valor del descuento
print("La compra fue",valorCompra,"con un descuento de",descuento ,"%","el valor final a pagar es",precioFinal)
#quinto, con el comando print se imprime el valor de la compra, el descuento, precio final y con la "," concateno las variables