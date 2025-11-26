products = {}
suppliers = {}

# Menú de opciones
options = """
1. Registrar producto
2. Registrar proveedor
3. Mostrar productos
4. Mostrar proveedores
5. Salir
"""

while True:
    print(options)
    option = input("Ingrese una opción: ")

    # 1) Registrar nuevo producto
    if option == "1":
        name = input("Nombre del producto: ").strip()

        # Evitar productos repetidos
        if name in products:
            print("El producto ya existe.\n")
            continue

        # Ingresar precio y stock
        try:
            price = float(input("Precio: "))
            stock = int(input("Cantidad en stock: "))
        except ValueError:
            print("Entrada inválida.\n")
            continue

        # Guardar producto
        products[name] = {"price": price, "stock": stock}
        print("Producto registrado.\n")

    # 2) Registrar nuevo proveedor
    elif option == "2":
        name = input("Nombre del proveedor: ").strip()

        # Evitar proveedores repetidos
        if name in suppliers:
            print("El proveedor ya existe.\n")
            continue

        phone = input("Teléfono del proveedor: ")

        supplied_products = []
        print("Ingrese los productos que suministra (escriba 'fin' para terminar):")

        # Añadir productos suministrados
        while True:
            p = input("Producto: ").strip()

            if p.lower() == "fin":
                break

            # Comprobar si el producto existe
            if p not in products:
                print("Ese producto no existe.\n")
                continue

            supplied_products.append(p)

        # Guardar proveedor
        suppliers[name] = {"phone": phone, "products": supplied_products}
        print("Proveedor registrado.\n")

    # 3) Mostrar productos
    elif option == "3":
        if not products:
            print("No hay productos.\n")
        else:
            for p, info in products.items():
                print(f"\nProducto: {p}")
                print(f"Precio: {info['price']}")
                print(f"Stock: {info['stock']}")
            print()

    # 4) Mostrar proveedores
    elif option == "4":
        if not suppliers:
            print("No hay proveedores.\n")
        else:
            for s, info in suppliers.items():
                print(f"\nProveedor: {s}")
                print(f"Teléfono: {info['phone']}")
                print("Productos suministrados:")
                for prod in info["products"]:
                    print(" -", prod)
            print()

    # 5) Salir del programa
    elif option == "5":
        break

    else:
        print("Opción inválida.\n")
