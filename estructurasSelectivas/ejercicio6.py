# Solicitamos al usuario ingresar el promedio del alumno y el costo de la pensión
promedio_Alumno = float(input("Ingrese el promedio del alumno: "))
costo_Pension = float(input("Ingrese el costo de la pensión: "))

# Verificamos si el promedio es mayor o igual a 9 para aplicar el descuento del 30%
if promedio_Alumno >= 9:
    descuento = 0.30 * costo_Pension
    monto_Pagar = costo_Pension - descuento
else:
    # Si el promedio es menor que 9, el alumno debe pagar la pensión completa más el 10% de IVA
    monto_Pagar = costo_Pension + 0.10 * costo_Pension

# Imprime el monto a pagar
print(f"El monto a pagar es: {monto_Pagar}")
