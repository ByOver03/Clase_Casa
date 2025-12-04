#Crear decorador llamado registrar_llamda
def registrar_llamada(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a la función: {func.__name__}")
        print(f"Argumentos: {args} {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"La función {func.__name__} ha terminado.")
        return resultado
    return wrapper

#funcion saludar con decorador
@registrar_llamada
def saludar(nombre):
    return f"Hola, {nombre}!"

#Funcion sumar con decorador
@registrar_llamada
def sumar(a, b):
    return a + b

#Menu
def menu():
    while True:
        print("Menu:")
        print("1. Saludar")
        print("2. Sumar dos números")
        print("3. Exit")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            nombre = input("Introduce tu nombre: ")
            print(saludar(nombre))
        elif opcion == "2":
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print(f"La suma es: {sumar(a, b)}")
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
menu()