matriz = [ 
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

for fila in matriz:
    suma = sum(fila[:3])
    fila[3] = suma

print(matriz)


[1, 1, 1, sum(matriz[0][:3])],

[2, 2, 2, sum(matriz[1][:3])],

[3, 3, 3, sum(matriz[2][:3])],

[4, 4, 4, sum(matriz[3][:3])]

