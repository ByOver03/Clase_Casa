# Funciones del sistema
def saludar():
    return "Hola!"

def despedir():
    return "Adiós!"

def ayuda():
    return "Comandos disponibles: hola, adios, ayuda"

# Diccionario de comandos
comandos = {
    "hola": saludar,
    "adios": despedir,
    "ayuda": ayuda
}

# Función para procesar un comando
def procesar(comando):
    if comando in comandos:        # Si el comando existe
        return comandos[comando]() # Ejecuta la función
    else:
        return "Comando no válido"

# Solicitar comando al usuario
entrada = input("Ingrese un comando: ")

# Procesar y mostrar resultado
resultado = procesar(entrada)
print(resultado)
