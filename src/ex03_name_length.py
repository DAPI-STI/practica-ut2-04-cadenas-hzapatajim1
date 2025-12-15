"""
Ejercicio 3: leer un nombre y mostrarlo en mayúsculas y cuántas letras tiene.

La función devolverá una tupla:
(nombre_en_mayusculas, numero_de_letras_sin_espacios)
"""

def name_upper_and_length(name: str) -> tuple[str, int]:
    """Devuelve (NAME_EN_MAYUSCULAS, numero_de_letras_sin_espacios)."""
    name_mayus = name.upper()
    num_letras = len(name.replace(" ", ""))
    return (name_mayus, num_letras)

print(name_upper_and_length("Ana Maria"))