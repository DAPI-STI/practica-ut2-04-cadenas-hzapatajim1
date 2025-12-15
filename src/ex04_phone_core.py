"""
Ejercicio 4: a partir de un teléfono con el formato "+34-<numero>-<extension>"
obtener solamente la parte central (el número), sin prefijo ni extensión.

Ejemplo: "+34-913724710-56" -> "913724710"
"""

def phone_core(s: str) -> str:
    """
    Recibe el teléfono como cadena y devuelve solo la parte central.
    """
    # Eliminar espacios al principio y al final
    s = s.strip()

    # Dividir en partes
    partes = s.split("-")
    if len(partes) != 3:
        raise ValueError("Formato incorrecto: deben ser 3 partes separadas por '-'")

    prefijo, numero, extension = partes

    # Validar prefijo
    if not prefijo.startswith("+"):
        raise ValueError("El prefijo debe comenzar con '+'")

    # Validar número central
    if not numero.isdigit():
        raise ValueError("La parte central debe ser numérica")

    return numero

print(phone_core("+34-913724710-56"))