#Decorador manejar_errores
def manejar_errores(func):
    def wrapper(a,b):
        try:
            return func(a,b)
        except ZeroDivisionError:
            print("Error: no se puede dividir por cero.")
            return None
        except Exception:
            print("Ha ocurrido un error en la operación.")
            return None
    return wrapper


#Funcion dividir con decorador
@manejar_errores
def dividir(a, b):
    return a / b


#Programa principal
a = None
b = None

while True:
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))

    resultado = dividir(a, b)
    if resultado is None:
        continue

    print(f"El resultado de dividir {a} entre {b} es: {resultado}")
    break