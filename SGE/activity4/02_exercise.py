precios = {
    "pan": 1.2,
    "leche": 0.9,
    "huevos": 2.1
}
def total_compra(compra):
    total = 0
    for producto, cantidad in compra.items():
        if producto in precios:
            total += precios[producto] * cantidad
        else:
            print(f"El producto {producto} no está en la lista de precios.")
    return total

compra = {}
num_productos = int(input("¿Cuántos productos desea ingresar? "))
for _ in range(num_productos):
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad comprada: "))
    compra[producto] = cantidad 
total = total_compra(compra)
print(f"El total de la compra es: {total} unidades monetarias.")