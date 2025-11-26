inventory = {}
option = 0
while option != 5:
# Agregar un producto de ejemplo al inventario
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Mostrar productos con stock bajo")
    print("4. Mostrar inventario completo")
    print("5. Salir")

    # excepción → opción inválida
    try:
        option = int(input("Seleccione una opción: "))
    except ValueError:
        print("Debe ingresar un número válido.\n")
        continue

    if option == 1:
        #Añadir un producto
        try:
            item_id = int(input("Ingrese el ID del producto: "))
        except ValueError:
            print("ID inválido.\n")
            continue

        # excepción → ID duplicado
        if item_id in inventory:
            print("Ese ID ya existe.\n")
            continue

        nombre = input("Ingrese el nombre del producto: ")

        try:
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese la cantidad en stock: "))
        except ValueError:
            print("Entrada inválida para precio o stock.\n")
            continue

        inventory[item_id] = {
            "nombre": nombre,
            "detalles": {
                "precio": precio,
                "stock": stock
            }
        }

    #Actualizar los productos por el ID
    elif option == 2:
        try:
            item_id = int(input("Ingrese el ID del producto a actualizar: "))
        except ValueError:
            print("ID inválido.\n")
            continue

        # excepción → ID no existe
        if item_id not in inventory:
            print("El ID del producto no existe en el inventario.")
            continue

        nombre = input("Ingrese el nuevo nombre del producto: ")

        try:
            precio = float(input("Ingrese el nuevo precio del producto: "))
            stock = int(input("Ingrese la nueva cantidad en stock: "))
        except ValueError:
            print("Entrada inválida.\n")
            continue

        inventory[item_id] = {
            "nombre": nombre,
            "detalles": {
                "precio": precio,
                "stock": stock
            }
        }

    #Mostrar los productos con un Stock inferior a 5
    elif option == 3:
        print("Productos con stock inferior a 5:")
        for item_id, item in inventory.items():
            detalles = item.get("detalles", {})
            stock = detalles.get("stock", 0)
            if stock < 5:
                nombre = item.get("nombre", "")
                precio = detalles.get("precio", "")
                print(f"ID: {item_id}  -  Nombre: {nombre}  -  Precio: {precio}  -  Stock: {stock}")

    #Mostrar los productos del inventario
    elif option == 4:
        print("Inventario completo:")
        import pprint
        if __name__ == "__main__":
            print("Inventario (estructura cruda):")
            pprint.pprint(inventory)
            print("\nProductos:")
            if not inventory:
                print("El inventario está vacío.")
            else:
                for item_id in sorted(inventory):
                    item = inventory[item_id]
                    nombre = item.get("nombre", "")
                    detalles = item.get("detalles", {})
                    precio = detalles.get("precio", "")
                    stock = detalles.get("stock", "")
                    print(f"ID: {item_id}  -  Nombre: {nombre}  -  Precio: {precio}  -  Stock: {stock}")

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
