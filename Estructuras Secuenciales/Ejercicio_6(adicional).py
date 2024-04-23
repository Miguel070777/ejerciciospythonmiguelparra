nombre_Estudiante = input("Ingrese el nombre del estudiante: ")
#Primero, Con el comando input le estamos pidiendo al estudiante que digite su nombre en teclado
calificacion_Actividades = float(input("Ingrese la calificación promedio de las actividades en clase en decimales (0-5): "))
calificacion_Proyecto = float(input("Ingrese la calificación del proyecto final en decimales (0-5): "))
calificacion_Evaluaciones = float(input("Ingrese la calificación promedio de las evaluaciones parciales en decimales (0-5): "))
# Segundo, De la linea 3 hasta la 5, se le pide al usuario que digite su calificacion en teclado
nota_Final = (calificacion_Actividades * 0.3) + (calificacion_Proyecto * 0.5) + (calificacion_Evaluaciones * 0.2)

print("La nota final de", nombre_Estudiante, "en algoritmia es:", nota_Final)
#Con el comando "print" se imprime las calificaciones de actividades, proyecto, evaluaciones y con "," concateno las variables