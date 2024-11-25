# Pruebas automatizadas de la clase BinarySearchTree

from BinarySearchTree import *
import sys

theTree = BinarySearchTree()
print('Se creó un árbol de búsqueda binario vacío')

keys = [44, 27, 33, 65, 57, 49, 55, 83, 71, 44, 27]
if len(sys.argv) > 1:  # Usar argumentos de línea de comandos si están presentes
   keys = [int(a) for a in sys.argv[1:]]

count = 0
for key in keys:
   print('Insertar la clave', key, 'en el árbol devuelve', 
         theTree.insert(key, count))
   count += 1

print('Se creó un árbol de búsqueda binario con', theTree.nodes(), 'nodos distribuidos en',
      theTree.levels(), 'niveles')
theTree.print()
root_data, root_key = theTree.root()
print('El nodo raíz del árbol tiene la clave:', root_key, 'y los datos:', root_data)

dkeys = [keys[i] for i in range(0, len(keys), 3)] + [37, 40]
for key in dkeys:
   print('Buscar la clave', key, 'devuelve', theTree.search(key))

for key in dkeys:
   print('Eliminar la clave', key, 'devuelve', theTree.delete(key))

print('El árbol de búsqueda binario ahora contiene',
      theTree.nodes(), 'nodos distribuidos en', theTree.levels(), 'niveles')
theTree.print()
root_data, root_key = theTree.root()
print('El nodo raíz del árbol tiene la clave:', root_key, 'y los datos:', root_data)
min_key, min_data = theTree.minNode()
print('La clave mínima es', min_key, 'con los datos', min_data)
max_key, max_data = theTree.maxNode()
print('La clave máxima es', max_key, 'con los datos', max_data)

print('Prueba del recorrido recursivo en orden utilizando la función de impresión')
theTree.inOrderTraverse()

for func in (theTree.traverse_rec, theTree.traverse):
   print('Usando el generador de recorrido {}recursivo'.format(
      '' if func == theTree.traverse_rec else 'no '))
   for order in ['pre', 'in', 'post']:
      print(' Recorrer el árbol utilizando el orden', order)
      for key, data in func(order):
         print(' {' + str(key) + ', ' + str(data) + '}', end='')
      print()
   print(' Comprobando la excepción para un tipo de recorrido desconocido')
   try:
      for item in func('orden incorrecto'):
         print(' De alguna manera el recorrido en "orden incorrecto" produjo:', item)
   except ValueError as e:
      print(' Se recibió el error de valor esperado:', e)

from random import *
random_tree = BinarySearchTree()
seed(3.14159)
for key, data in theTree.traverse('pre'):
   random_tree.insert(key, randrange(1000))
print('Un árbol con las mismas claves pero con datos aleatorios:')
random_tree.print(indentBy=2)

total, count = 0, 0
for key, data in random_tree.traverse('pre'):
   total += data
   count += 1
average = total / count
below_average = []
for key, data in random_tree.traverse('in'):
   if data <= average:
      below_average.append((key, data))
print('Los elementos del árbol con datos menores o iguales al promedio', average, 'son:', 
      below_average)
below_average2 = [
   (key, data) for key, data in random_tree.traverse('in')
   if data <= average]
print('La comprensión de lista', 
      '' if below_average == below_average2 else 'no',
      'coincide')
