def identificar_tipo(valor):
    tipo = type(valor)
    if tipo == str:
        return "string"
    elif tipo == int:
        return "int"
    elif tipo == float:
        return "float"
    elif tipo == list:
        return "list"
    else:
        return "Tipo desconocido"

valores = ["Hola Mundo", [1, 10, 100], -25, 1.167, ["Hola", "Mundo"], ' ']

for valor in valores:
    print(f'El valor "{valor}" es de tipo {identificar_tipo(valor)}')