numero=int(input("ingresa un numero"))
if numero>=1 and numero<=10:
    for i in range(1,11):
        resultado=numero*i
        print(numero,"x",i,"=",resultado)
else:
    print("el numero debe estar entre el 1 y el 10")