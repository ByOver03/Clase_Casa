# Lista de alumnos
alumnos = [
    {"nombre": "Ana", "nota": 8},
    {"nombre": "Luis", "nota": 4},
    {"nombre": "Marta", "nota": 6}
]

# Función: aprobado → nota >= 5
def aprobado(nota):
    return nota >= 5

# Función: excelente → nota >= 9
def excelente(nota):
    return nota >= 9

# Función para filtrar alumnos según un criterio
def filtrar_alumnos(lista, funcion_criterio):
    nueva_lista = []
    for alumno in lista:
        if funcion_criterio(alumno["nota"]):
            nueva_lista.append(alumno)
    return nueva_lista

# Preguntar al usuario qué filtro quiere aplicar
opcion = input("¿Desea ver alumnos 'aprobados' o 'excelentes'? ").lower()

# Seleccionar la función correspondiente
if opcion == "aprobados":
    resultado = filtrar_alumnos(alumnos, aprobado)
elif opcion == "excelentes":
    resultado = filtrar_alumnos(alumnos, excelente)
else:
    print("Opción no válida.")
    resultado = []

# Mostrar resultado
print("\nLista filtrada:")
for alumno in resultado:
    print(f"{alumno['nombre']} - Nota: {alumno['nota']}")
