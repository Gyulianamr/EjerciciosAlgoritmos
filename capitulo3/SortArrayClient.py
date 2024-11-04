from SortArray import Array
import timeit
import random

def initArray(size=100, maxValue=100, seed=random.random()):
    """Crea un Array del tamaño especificado con una secuencia fija de
       elementos 'aleatorios'."""
    arr = Array(size)                   # Crea el objeto Array
    random.seed(seed)                   # Establece el generador de números aleatorios
    for i in range(size):               # Para ponerlo en un estado conocido, luego bucle
        arr.insert(random.randrange(maxValue))  # Inserta números aleatorios
    return arr                          # Devuelve el Array lleno

# Inicializa el array una vez
arr = initArray()
print("Array que contiene", len(arr), "elementos:\n", arr)

# Mide el tiempo de diferentes métodos de ordenamiento
sort_methods = ['bubbleSort', 'selectionSort', 'insertionSort']

for method in sort_methods:
    elapsed = timeit.timeit(f'arr.{method}()', number=100, globals=globals())
    print(f'{method} tomó {elapsed:.6f} segundos')

# 3.1 Ordenamiento por burbuja bidireccional
arr.Bidireccionalburb()
print("Array ordenado usando el método de burbuja bidireccional:", arr)

# 3.2 Cálculo de la mediana
median_value = arr.median()
print("Valor de la mediana:", median_value) 

# 3.3 Eliminación de duplicados
arr.deduplicate()
print("Array sin duplicados:", arr)

# 3.4 Ordenamiento par-impar
passes = arr.oddEvenSort()
print("Array ordenado usando el método par-impar:", arr)
print("Número de pasadas:", passes)

# 3.5 Ordenamiento por inserción (nuevamente, solo para demostración)
total_copias, total_comparaciones = arr.insertionSort()

# Imprimir el total de copias y comparaciones
print(f"\nTotal copias: {total_copias}, Total comparaciones: {total_comparaciones}")

# 3.6 Ordenamiento por inserción y eliminación de duplicados
arr = initArray()
print("Antes de ordenar y eliminar duplicados:", arr)
arr.insertionSortAndDedupe()
print("Después de ordenar y eliminar duplicados:", arr)



