#Crear clase Producto
# Atributos:
#   nombre- string
#   precio- float
#   stock- int


# Reglas:
#   Si el precio inicial es negativo, ponlo a 0 y muestra un warning
#   Si el stock inicial es negativo, ponlo a 0 y muestra un warning

# Metodos:
#   mostrar_info(): muestra nombre, precio y stock
#   actualizar_stock(cantidad): añade la cantidad, puede ser negativa, si es negativa no lo actualices y muestra un warning
#   aplicar_descuento(porcentaje):aplica el descuento solo si es entre 0 y 100, ajusta el precio basado en el descuento por porcentaje

# Main:
#   Pedir al usuario por el producto, nombre precio y stock usando try/except para la conversion numerica
#   Muestra la informacion inicial del producto
#   Pide una cantidad para modificar el stock
#   Pide un porcentaje para aplicar un descuento
#   Muestra la informacion final del producto