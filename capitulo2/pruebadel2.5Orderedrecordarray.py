from OrderedRecordArray import OrderedRecordArray, identity

# Crear un arreglo de registros ordenados con tamaño inicial de 5 y un factor de crecimiento (ejemplo: 2)
growth_factor = 2
ordered_array = OrderedRecordArray(5, growth_factor)

# Probar inserciones
print("Insertando registros...")
ordered_array.insert("apple")
ordered_array.insert("banana")
ordered_array.insert("cherry")
print("Estado después de inserciones:", ordered_array)

# Probar la longitud
print("Longitud del arreglo:", len(ordered_array))

# Probar la recuperación
print("Elemento en el índice 1:", ordered_array.get(1))

# Probar la eliminación
print("Eliminando 'banana'...")
ordered_array.remove("banana")
print("Estado después de eliminación:", ordered_array)

# Crear otro arreglo de registros ordenados
ordered_array2 = OrderedRecordArray(5, growth_factor)
ordered_array2.insert("date")
ordered_array2.insert("fig")
ordered_array2.insert("grape")
print("Segundo arreglo:", ordered_array2)

# Probar la fusión de arreglos
print("Fusionando arreglos...")
ordered_array.merge(ordered_array2)
print("Estado después de fusionar:", ordered_array)

# Probar el recorrido
print("Recorriendo el arreglo combinado:")
ordered_array.traverse()
