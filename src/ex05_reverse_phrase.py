"""
Ejercicio 5: escribir una frase y mostrarla invertida (carácter a carácter).
"""

def reverse_phrase(s: str) -> str:
    """Devuelve la frase invertida (carácter a carácter)."""
    return s[::-1]

frase = "Hola mundo"
print(reverse_phrase(frase))