# Function that receives named arguments
def create_profile(**kwargs):
    perfil = ""

    for clave, valor in kwargs.items():
        perfil += f"{clave}: {valor}, "

    # Remove the last comma + space
    perfil = perfil.rstrip(", ")

    return perfil


# Call the function with at least 3 named parameters
perfil_generado = create_profile(nombre="Ana", edad=22, ciudad="Madrid")

print("\nPerfil generado:")
print(perfil_generado)
