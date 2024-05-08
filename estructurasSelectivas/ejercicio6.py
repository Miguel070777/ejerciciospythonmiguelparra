# Solicitamos al usuario ingresar el promedio del alumno y el costo de la pensión
promedioAlumno = float(input("Ingrese el promedio del alumno: "))
costoPension = float(input("Ingrese el costo de la pensión: "))

# Verificamos si el promedio es mayor o igual a 9 para aplicar el descuento del 30%
if promedioAlumno >= 9:
    descuento = 0.30 * costoPension
    montoPagar = costoPension - descuento
else:
    # Si el promedio es menor que 9, el alumno debe pagar la pensión completa más el 10% de IVA
    montoPagar = costoPension + 0.10 * costoPension

# Imprime el monto a pagar
print(f"El monto a pagar es: {montoPagar}")
