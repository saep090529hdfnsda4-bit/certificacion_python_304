#creando un diccionario
persona={
    "nombre":"pedro",
    "edad":17,
    "profesion":"programador",
    "estudiante":True
}
print(persona)
#accediendo a un valor especifico
print(persona["edad"])
#se puede usar el metodo get()
#es util porque no marca error si el valor no existe
print(persona.get("profesion"))
#modificar un valor existente
persona["edad"]=18
print(persona["edad"])