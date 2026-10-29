#creando una matriz
numeros=[
    [1,2,3],#fila 0
    [4,5,6],#fila 1
    [7,8,9],#fila 2
]
#obteniendo el numero de filas 
filas=len(numeros)#filas=3
#obteniendo el numero de columnas
columnas=len(numeros[0])#columnas=2
#ciclo externo para los indices de las filas(i)
for i in range(0,3):
    #ciclo interno para los indices para las columnas(j)
    for j in range(0,3):
        print(f"[{i}][{j}]={numeros[i][j]}")