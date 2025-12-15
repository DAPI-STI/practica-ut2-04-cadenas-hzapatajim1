"""
Ejercicio 9: leer una fecha (día, mes, año) introducida como "dd/mm/aaaa"
y mostrar cada componente por separado.

La función:

Recibe un string con formato "d/m/aaaa" o "dd/mm/aaaa".

Devuelve (dia, mes, año) como enteros.

Si el formato o los rangos son incorrectos, lanza ValueError.
"""

def parse_date(date_str: str) -> tuple[int, int, int]:
    """Devuelve (día, mes, año) como enteros a partir de una cadena d/m/aaaa."""
    parts = date_str.strip().split("/")
    if len(parts) != 3:
        raise ValueError("La fecha debe tener el formato d/m/aaaa")

    try:
        dia = int(parts[0])
        mes = int(parts[1])
        año = int(parts[2])
    except ValueError:
        raise ValueError("Día, mes y año deben ser números enteros")

    if not (1 <= dia <= 31):
        raise ValueError("El día debe estar entre 1 y 31")
    if not (1 <= mes <= 12):
        raise ValueError("El mes debe estar entre 1 y 12")
    if año <= 0:
        raise ValueError("El año debe ser mayor que 0")

    return dia, mes, año

print(parse_date("2/12/2025")) 
print(parse_date("31/01/1990")) 