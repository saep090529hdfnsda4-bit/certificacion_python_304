#cadena y concatenacion (+)
cadena1='hola'
cadena2='mundo'
multilinea="""esto es una cadena
de varias lineas"""
print(cadena1 + cadena2)#print(f"{cadena1}")
#cadenas y repeticion
eco="ja"*67
print(eco)
#cambiar una cadena de minuscula a mayuscula
tu_nombre='pedro'
print(tu_nombre.upper())
#cambiar una de cadena de mayuscula a minuscula
print(tu_nombre.lower())
#remplazar texto en una cadena
frase="me gusta  programacion"
print(frase.replace("programacion"," filosofia"))
#formato de cadenas  (f-string)
edad=17
nombre='pedro'
mensaje=f"hola,me llamo\n{nombre}\ny tengo\n{edad}años"
print(mensaje)
#contar los caracteres de una cadena 
texto= "¡felicidades por aun continuar en el cecy!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#comprobar si  un texto contiene una palabra
oracion="aprender python es divertido"
if "java" in oracion:
    print("encontrado")
else:
    print("no esta")
    #validar contenido de una cadena
nlista="pedro"
print(nlista.isalpha())
