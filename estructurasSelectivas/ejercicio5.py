#De la linea 2 hasta la 3 pedimos al usuario que digite esos datos
genero=input("digite el genero (masculino o femenino): ")
edad=int(input("digite la edad que tiene: "))
#de la linea 5 hasta la 9 decidimos que si es femenino restemos 220 menos la edad dividido en 10 y en el hombre lo mismo pero con 20 y que imprima sus numeros de pulsaciones 
if genero == " femenino":
    pulsaciones= (220 - edad)/10   
if genero =="masculino":
    pulsaciones=  (210 - edad)/10
print( f"el numero de sus pulsaciones es: {pulsaciones}")