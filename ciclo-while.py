# Ciclo while
# El ciclo while se ejecuta mientras una condición sea verdadera. 
# Es útil cuando no se sabe de antemano cuántas veces se debe ejecutar el bloque de código.

#Ejemplo
contador = 0
while contador < 5:
    print(contador)
    contador += 1

#Ejemplo con una lista
frutas = ["manzana", "banana", "cereza"]
indice = 0 
while indice < len(frutas):
    print(frutas[indice])
    indice += 1

#Ejemplo con una tupla
numeros = (1, 2, 3, 4, 5)  
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice += 1

#Ejemplo con un diccionario
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Buenos Aires"}
claves = list(persona.keys()) # keys() devuelve una vista de las claves del diccionario. Al convertirlo a una lista, podemos acceder a las claves por su índice.
indice = 0
while indice < len(claves):
    clave = claves[indice]
    valor = persona[clave]
    print(f"{clave}: {valor}")
    indice += 1