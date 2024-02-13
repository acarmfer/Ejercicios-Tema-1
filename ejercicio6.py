def invertir_cadena(cadena):
    return cadena[::-1]

def dividir_cadena(cadena):
    return cadena.split(',')

def formatear_salida(nombre, nota):
    return f"{nombre} ha sacado un Nota de {nota}."

cadena = "zeréP nauJ,01"

cadena_invertida = invertir_cadena(cadena)
nombre, nota = dividir_cadena(cadena_invertida)
resultado = formatear_salida(nombre, nota)

print(resultado)