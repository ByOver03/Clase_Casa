# Function that processes a variable number of arguments
def sum_numbers(*args):
    # Keep only numeric values
    numeros = []
    for x in args:
        if isinstance(x, int) or isinstance(x, float):
            numeros.append(x)

    # If there are no numeric values
    if len(numeros) == 0:
        return {"cantidad": 0, "suma": 0, "promedio": 0}

    cantidad = len(numeros)
    suma_total = sum(numeros)
    promedio = suma_total / cantidad

    return {
        "cantidad": cantidad,
        "suma": suma_total,
        "promedio": promedio
    }


valores_usuario = input("Ingrese varios valores separados por espacios: ").split()

# Convert values to numbers when possible
valores_convertidos = []
for valor in valores_usuario:
    try:
        if "." in valor:
            valores_convertidos.append(float(valor))
        else:
            valores_convertidos.append(int(valor))
    except:
        valores_convertidos.append(valor)  # keep non-numerics as text

# Call the function using *
resultado = sum_numbers(*valores_convertidos)

print("\nResultado de sum_numbers:")
print(resultado)
