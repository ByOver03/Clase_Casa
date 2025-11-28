def analizar_texto(texto):
    vocal = 0
    consonante = 0
    # Convertir texto a minuscula
    texto = texto.lower()
    caracteres_eliminar = ".,;:!?'\"()[]{} "
    # eliminar (.,;:!?"'()[]{} ) y ahora también el espacio " "
    for char in caracteres_eliminar:
        texto = texto.replace(char, "")

    # Variable para caracter más repetido
    char_mas_repetido = ""
    max_repeticiones = 0

    for char in texto:
        # -numero de vocales
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            vocal += 1
        # -numero de consonantes
        elif char.isalpha() and char not in "aeiou":
            consonante += 1

        # -caracter mas frecuente
        rep = texto.count(char)
        if rep > max_repeticiones:
            max_repeticiones = rep
            char_mas_repetido = char

    # -numero de caracteres
    print(texto)
    print("Numero de caracteres:", len(texto))
    print("Numero de vocales:", vocal)
    print("Numero de consonantes:", consonante)
    print("Caracter más repetido:", char_mas_repetido, "(", max_repeticiones, "veces )")


analizar_texto(input("Ingrese un texto para analizar: "))
