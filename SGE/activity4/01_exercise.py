#function analizar_texto(texto):


#analizar  lo siguiente:





#Preguntar al usuario por un texto
#Llamar a la funcion analizar_texto con el texto proporcionado
#Imprimir los resultados del analisis

# function analizar_texto(texto):


# analizar  lo siguiente:




# Preguntar al usuario por un texto
# Llamar a la funcion analizar_texto con el texto proporcionado
# Imprimir los resultados del analisis


def analizar_texto(texto):
    vocal = 0
    consonante = 0
    # Convertir texto a minuscula
    texto = texto.lower()
    caracteres_eliminar = ".,;:!?'\"()[]{}"
    # eliminar (.,;:!?"'()[]{} )
    for char in caracteres_eliminar:
        texto = texto.replace(char, "")

    for char in texto:
        # -numero de vocales
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            vocal += 1
        # -numero de consonantes
        elif char.isalpha() and char not in "aeiou":
            consonante += 1
        #-caracter mas frecuente
    # -numero de caracteres
    print(texto)
    print("Numero de caracteres:", len(texto))
    print("Numero de vocales:", vocal)
    print("Numero de consonantes:", consonante)


analizar_texto(input("Ingrese un texto para analizar: "))

