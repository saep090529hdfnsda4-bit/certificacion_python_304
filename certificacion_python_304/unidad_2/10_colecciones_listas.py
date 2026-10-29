carrito=[]
num_productos=int(input("ingresa el numero de productos"))
for i in range (num_productos):
    productos=input("ingresa el producto a tu carrito")
    carrito.append(productos)
print("lista creada correctamente")
print(f"tu carrito contiene{carrito}")
carrito[0]="chetos"
print(carrito[0])
print(carrito[1])
print(carrito)