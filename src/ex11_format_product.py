"""
Ejercicio 11: formatear información de un producto (nombre, precio, unidades).

La función:

Recibe nombre (str), precio (float) y unidades (int).

Devuelve una cadena formateada con:
nombre
precio unitario con 6 dígitos enteros y 2 decimales
unidades con 3 dígitos (relleno con ceros)
coste total (precio * unidades) con 8 enteros y 2 decimales
"""
def format_product(name: str, price: float, units: int) -> str:
    """Devuelve una descripción de producto formateada con anchuras fijas."""
    total = price * units
    return (
        f"{name}\n"
        f"Precio unitario: {price:08.2f}\n"
        f"Unidades: {units:03d}\n"
        f"Coste total: {total:010.2f}"
    )
print(format_product("Manzanas", 123.45, 7))