# Tuplas: no se pueden modificar, son inmutables
 
provincias = ('Buenos Aires', 'Córdoba', 'Santa Fe', 'Mendoza', 'Tucumán')
print(provincias[0])
#for provincia in provincias:
#    print(provincia)

# Set: no se pueden modificar, son inmutables, no permiten elementos repetidos
colores = {'rojo', 'verde', 'azul', 'amarillo', 'rojo'}
print(colores)
# para agregar un elemento a un set se utiliza el método add()
colores.add('negro')  
# para quitar un elemento a un set se utiliza el método remove()
colores.remove('rojo')

# Diccionario: colección de pares clave-valor, donde cada clave es única
persona = {
    "nombre": "Roberto",
    "edad": 45,
    "ciudad": "Buenos Aires"
}
print(persona["edad"])  # Acceder al valor de una clave
persona["edad"] = 31  # Modificar el valor de una clave
print(persona["edad"])  # Acceder al valor de una clave

# Funciones 
def suma(a, b):
    return a + b
resultado = suma(5, 3)
print(resultado)