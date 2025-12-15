"""
Ejercicio 10: leer una lista de productos separados por comas y mostrar cada uno en una línea.

La función:

Recibe una cadena tipo "pan, leche, huevos".

Devuelve una lista con ["pan", "leche", "huevos"], sin espacios sobrantes.
"""

def split_products(csv_line: str) -> list[str]:
    """Devuelve una lista de productos sin espacios extra a partir de una línea CSV simple."""
    productos = csv_line.split(",")
    # Limpiar espacios alrededor de cada producto
    return [p.strip() for p in productos if p.strip()]  # elimina posibles entradas vacías

linea = "pan, leche, huevos"
print(split_products(linea))
