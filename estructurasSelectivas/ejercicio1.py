#De la linea 2 hasta la linea 1o le pedimos que ingrese los datos
nombEstudiante= input("Ingrese el Nombre del Estudiante: ")

califi_1 = int(input("Ingrese la Primera Nota (0-100): "))


califi_2 = int(input("Ingrese la Segunda Nota (0-100): "))


califi_3 = int(input("Ingrese la Tercera Nota(0-100): "))
#Aca decimos que si la calificacion es mayor o igual al 101 imprima que no se admite como una nota valida
if  califi_1 >= 101 or califi_2 >= 101 or califi_3 >= 101:
    print(f"En Alguna de las Notas Ingresadas un Numero es Mayor a 100 no se admite como una nota valida")
#aca decimos que sume las calificaciones y las divida por las mismas
else:
    caliCasi = (califi_1) + (califi_2) + (califi_3)

    califiFinal = caliCasi/3

    formatearNumero = str(califiFinal).split('.')[0] #Con este atributo formateamos el numero para que no salgan ceros de más

    if califiFinal >= 70: #aca decimos que si la calificacion final es mayor o igual que 70 imprima la nota final, el nombre del estudiante y si aprobo o reprobo
        print(f"La Nota Final fue de: {formatearNumero} El/La Estudiante {nombEstudiante} Aprobó 🎉")
    
    else:
        print(f"La Nota Final fue de: {formatearNumero} El/La Estudiante {nombEstudiante} Reprobó 😓")


