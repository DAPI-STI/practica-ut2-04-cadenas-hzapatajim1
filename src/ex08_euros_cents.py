"""
Ejercicio 8: leer un precio con dos decimales y mostrar euros y céntimos por separado.

La función:

Recibe una cadena como "123.45" o "123,45".

Devuelve una tupla (euros, centimos) como enteros.

Valida que haya exactamente dos decimales; en caso contrario, ValueError.
"""

def euros_cents(price_str: str) -> tuple[int, int]:
    """Separa la parte entera (euros) y los céntimos a partir de una cadena."""
    # Normalizar coma a punto
    price_str = price_str.replace(",", ".").strip()

    partes = price_str.split(".")
    if len(partes) != 2:
        raise ValueError("El precio debe tener exactamente dos decimales separados por '.' o ','")

    euros_str, centimos_str = partes

    if len(centimos_str) != 2 or not euros_str.isdigit() or not centimos_str.isdigit():
        raise ValueError("El precio debe tener exactamente dos decimales y ambas partes deben ser números")

    return int(euros_str), int(centimos_str)

print(euros_cents("123.45"))  
print(euros_cents("67,89"))