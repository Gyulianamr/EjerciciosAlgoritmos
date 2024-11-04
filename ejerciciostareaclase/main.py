import random
from Pila import Pila  # Import the Pila class
from Cola import Cola  # Import the Cola class

maxSize = 100  
pila = Pila(maxSize)
cola = Cola(maxSize)


opcion = input("¿Quieres usar pila o cola? (pila/cola): ").strip().lower()

if opcion == "pila":
    for _ in range(maxSize):
        pila.push(random.randint(1, 100))  

    print("Contenido de la pila:", pila) 
    resultados = pila.contar_sumar_pares_impares() 
    print("Suma de pares:", resultados["suma_pares"])
    print("Promedio de pares:", resultados["promedio_pares"])
    print("Cantidad de pares:", resultados["conteo_pares"])
    print("Suma de impares:", resultados["suma_impares"])
    print("Promedio de impares:", resultados["promedio_impares"])
    print("Cantidad de impares:", resultados["conteo_impares"])

elif opcion == "cola":
    for _ in range(maxSize):
        cola.enqueue(random.randint(1, 100)) 

    print("Contenido de la cola:", cola)  
    resultados = cola.contar_sumar_pares_impares() 
    print("Suma de pares:", resultados["suma_pares"])
    print("Promedio de pares:", resultados["promedio_pares"])
    print("Cantidad de pares:", resultados["conteo_pares"])
    print("Suma de impares:", resultados["suma_impares"])
    print("Promedio de impares:", resultados["promedio_impares"])
    print("Cantidad de impares:", resultados["conteo_impares"])
   
    



else:
    print("Opción no válida. Por favor elige 'pila' o 'cola'.")
