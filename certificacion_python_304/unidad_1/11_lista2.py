#declarando una lista 
try:
   nombres=["sofia","ivon","litzy","sherlyn","nora"]
   calificaciones=[7,8,9,6,5,6]
   print("nombre:",nombres[2],"calificaciones:",calificaciones[2])
   print("nombre:",nombres[4],"calificaciones:",calificaciones[4])

except IndexError:
    print("no se encontro el nombrey/o la calificacion")