#De la linea 2 hasta la 4 le decimos al usuario que ingrese los datos
edad = float(input("Ingrese la edad en años: "))
sexo = input("Ingrese el sexo (mujer o hombre): ")
nivelHemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))

tieneAnemia = False #De la linea 6 hasta la 31 decidimos que si el nivel de hemoglobina es mayor o menor que lo asignado, decida si tiene anemia o no con el atributo TRUE

if edad <= 1/12:
    if nivelHemoglobina < 13 or nivelHemoglobina > 26:
        tieneAnemia = True
elif 1/12 < edad <= 6/12:
    if nivelHemoglobina < 10 or nivelHemoglobina > 18:
        tieneAnemia = True
elif 6/12 < edad <= 12/12:
    if nivelHemoglobina < 11 or nivelHemoglobina > 15:
        tieneAnemia = True
elif 1 < edad <= 5:
    if nivelHemoglobina < 11.5 or nivelHemoglobina > 15:
        tieneAnemia = True
elif 5 < edad <= 10:
    if nivelHemoglobina < 12.6 or nivelHemoglobina > 15.5:
        tieneAnemia = True
elif 10 < edad <= 15:
    if nivelHemoglobina < 13 or nivelHemoglobina > 15.5:
        tieneAnemia = True
elif sexo == "mujer" and edad > 15:
    if nivelHemoglobina < 12 or nivelHemoglobina > 16:
        tieneAnemia = True
elif sexo == "hombre" and edad > 15:
    if nivelHemoglobina < 14 or nivelHemoglobina > 18:
        tieneAnemia = True
#Aca hacemos una desicion de que si tiene anemia imprima que es positivo y si no, lo contrario
if tiene_Anemia:
    print("Resultado: Positivo para anemia.")
else:
    print("Resultado: Negativo para anemia.")
