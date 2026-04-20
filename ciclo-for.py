# Ciclo for
# El ciclo for se utiliza para iterar sobre una secuencia (como una lista, una tupla,
# un diccionario, un conjunto o una cadena de caracteres) o cualquier otro objeto iterable.


#Ejemplo 
for i in range(5):
    print(i)

#Ejemplo con lista
frutas = ["manzana", "banana", "cereza"] # Una lista es una colección ordenada y mutable de elementos. Se define con corchetes [] y puede contener elementos de diferentes tipos.
for fruta in frutas:
    print(fruta)

#Ejemplo con tupla 
numeros = (1, 2, 3, 4, 5) # Una tupla es una colección ordenada e inmutable de elementos. Se define con paréntesis () y puede contener elementos de diferentes tipos.
for numero in numeros:
    print(numero)
    
#Ejemplo con diccionario 
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Buenos Aires"} # Un diccionario es una colección de pares clave-valor. Se define con llaves {} y cada par clave-valor se separa por dos puntos :.
for clave, valor in persona.items(): # items() devuelve una vista de los pares clave-valor del diccionario.
    print(f"{clave}: {valor}") # f hace referencia a una cadena formateada, que permite incluir expresiones dentro de llaves {}. En este caso, se incluyen las variables clave y valor para imprimir cada par clave-valor del diccionario.


#Ejemplo con conjunto
conjunto = {1, 2, 3, 4, 5} # Un conjunto es una colección no ordenada de elementos únicos.
for elemento in conjunto:
    print(elemento)

#Ejemplo con cadena de caracteres
palabra = "Hola" # Una cadena de caracteres es una secuencia de caracteres encerrada entre comillas simples '' o dobles "".
for letra in palabra:
    print(letra)    
