# Función analizar(lista)
def analizar(lista):
    # 1. Si la lista está vacía → excepción
    if len(lista) == 0:
        raise Exception("La lista está vacía.")

    # 2. Filtrar solo los valores numéricos
    lista_numerica = []
    for elemento in lista:
        if isinstance(elemento, int) or isinstance(elemento, float):
            lista_numerica.append(elemento)

    # 3. Si no hay valores numéricos → excepción
    if len(lista_numerica) == 0:
        raise Exception("No hay valores numéricos en la lista.")

    # 4. Calcular estadísticas
    cantidad = len(lista_numerica)
    suma_total = sum(lista_numerica)
    promedio = suma_total / cantidad
    maximo = max(lista_numerica)
    minimo = min(lista_numerica)

    # 5. Devolver diccionario
    return {
        "cantidad": cantidad,
        "suma": suma_total,
        "promedio": promedio,
        "maximo": maximo,
        "minimo": minimo
    }


# 1. Preguntar cuántos elementos desea ingresar
try:
    n = int(input("¿Cuántos elementos desea ingresar? "))
except ValueError:
    print("Error: You must enter a valid number.")
    n = 0   # Asignar 0 en caso de error

# 2. Pedir los valores y guardarlos en la lista
lista = []

if n > 0:
    print("Ingrese los elementos (numéricos o no numéricos):")
    for i in range(n):
        valor = input(f"Elemento {i+1}: ")
        # Guardamos el valor tal cual, sin convertir
        try:
            # Intentar convertir a número
            if "." in valor:
                lista.append(float(valor))
            else:
                lista.append(int(valor))
        except ValueError:
            # Si no se puede convertir → guardar como texto
            lista.append(valor)

# 3 y 4. Analizar la lista y mostrar resultados
try:
    resultado = analizar(lista)
    print("\nResultados del análisis:")
    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")
except Exception as e:
    print("\nError durante el análisis:")
    print(e)
