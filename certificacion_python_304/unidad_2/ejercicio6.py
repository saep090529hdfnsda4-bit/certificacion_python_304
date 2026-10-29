tabla = [
    ["nombre","edad","calificacion"],
    ["pedro",17,7.5],
    ["sofia",15,8.5],
    ["ivonne",16,9.5],
    ["ivan",16,6.5],
    ["litzy",15,8.0],
    ["diana",15,7.0],
    ["sherlyn",16,9.0],
    ["amanda",16,9.0],
    ["eusebia",15,8.8],
    ["nora",16,6.7]
]
nombre=input("introduce un nombre")
filas=len(tabla)
columnas=len(tabla[0])
for i in range(filas):
    for j in range(columnas):
        if tabla[i][j] == nombre:
            print(f"nombre encontrado en la posicion[{i}][{j}]")
            print(f"edad{tabla}[i][j]")
            print(f"calificacion{tabla}[i][j]")