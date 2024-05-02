cantidad_Total = float(input("ingrese el monto total de la compra:")) # Asignamos el monto total para empezar y como vamos a trabajar con decimales ponemos float
if cantidad_Total_Total > 500000:
    propio = cantidad_Total * 0.55
    prestamo_Banco = monto_Total * 0.30
    credito_Fabricante = monto_Total        # Ingresamos las variables y asignamos el porcentaje que nos indican en el ejercicio
else:
    propio = cantidad_Total * 0.70
    credito_Fabricante = cantidad_Total - propio
    prestamo_Banco = 0                        # Si el monto no excede los 500.000 entonces entonces ingresamos el monto total por el porcentaje de la empresa
    
interes_Credito_fabricante = credito_Fabricante * 0.20    # Asignamos una variable nueva que seria el interes del fabricante que seria el 20%
total_Pago_credito_fabricante = credito_Fabricante + interes_Credito_fabricante
print("Detalle del pago: ")
print(f"Propio: COP{propio}")
print(f"Prestamo del banco: COP{prestamo_Banco}")
print(f"Interes por credito al fabricante: COP{interes_Credito_fabricante}")
print(f"Total a pagar al fabricante: COP{total_Pago_credito_fabricante}")
# Por ultimo solo queda imprimir para que nos indique el resultado de las variables 
