# De la linea 1 hasta la 2 le pedimos que ingrese los siguientes datos en cm: Valor de la altura, base
base=int(input("Ingrese el valor de la altura del rectangulo en cm: "))
altura=int(input("Ingrese el valor de la base del rectangulo en cm: "))
perimetro=(base*2) + (altura*2)
#Segundo, toca multiplicar la base y la altura por 2 y sumarla
area= base * altura
#tercero para el area se multiplica la base por la altura
print("El perímetro del rectángulo es: ",perimetro,"cm" " el area del rectangulo es: ",area,"cm")
#cuarto, Con el comando "print" el enunciado  y concateno las variables