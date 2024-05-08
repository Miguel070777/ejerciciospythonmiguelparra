cantidadTotal = float(input("ingrese el monto total de la compra:")) # Asignamos el monto total para empezar y como vamos a trabajar con decimales ponemos float
if cantidadTotal > 500000:
    propio = cantidadTotal * 0.55
    prestamoBanco = montoTotal * 0.30
    creditoFabricante = montoTotal        # Ingresamos las variables y asignamos el porcentaje que nos indican en el ejercicio
else:
    propio = cantidadTotal * 0.70
    credito_Fabricante = cantidadTotal - propio
    prestamo_Banco = 0                        # Si el monto no excede los 500.000 entonces entonces ingresamos el monto total por el porcentaje de la empresa
    
interesCreditofabricante = creditoFabricante * 0.20    # Asignamos una variable nueva que seria el interes del fabricante que seria el 20%
totalPagocreditofabricante = creditoFabricante + interesCreditofabricante
print("Detalle del pago: ")
print(f"Propio: COP{propio}")
print(f"Prestamo del banco: COP{prestamoBanco}")
print(f"Interes por credito al fabricante: COP{interesCreditofabricante}")
print(f"Total a pagar al fabricante: COP{total_Pagocreditofabricante}")
# Por ultimo solo queda imprimir para que nos indique el resultado de las variables 
