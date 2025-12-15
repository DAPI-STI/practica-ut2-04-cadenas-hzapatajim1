"""
Ejercicio 6: pedir una frase y una vocal y mostrar la frase con la vocal en mayúsculas.

La función debe:

Recibir una frase y una vocal (a, e, i, o, u) en cualquier caso.

Devolver la frase sustituyendo esa vocal (mayúscula/minúscula) por su versión en mayúscula.

Si la vocal no es válida, lanzar ValueError.
"""

def emphasize_vowel(phrase: str, vowel: str) -> str:
    """
    Convierte a mayúscula todas las apariciones de vowel en la frase.
    """
    vowel = vowel.lower()
    if len(vowel) != 1 or vowel not in "aeiou":
        raise ValueError("La vocal no es válida. Debe ser una de 'a', 'e', 'i', 'o', 'u'.")

    result = ""
    for char in phrase:
        if char.lower() == vowel:
            result += char.upper()
        else:
            result += char

    return result

frase = "Hola mundo"
vocal = "o"
print(emphasize_vowel(frase, vocal))
