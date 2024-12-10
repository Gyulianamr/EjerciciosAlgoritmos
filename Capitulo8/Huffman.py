"""Escribir un programa para implementar la codificación y decodificación de Huffman. 
Debe hacer lo siguiente: Aceptar un mensaje de texto (cadena). Cree un árbol de Huffman para este mensaje. 
Cree una tabla de códigos. Codifique el mensaje de texto en binario. Decodifique el mensaje binario de nuevo en texto. 
Muestra el número de bits en el mensaje binario y el número de caracteres en el mensaje de entrada. 
Si el mensaje es corto, el programa debería ser capaz de mostrar el árbol de Huffman después de crearlo. 
Puede utilizar variables de cadena de Python para almacenar mensajes binarios como arreglos de los caracteres 1 y 0. 
No se preocupe por hacer una manipulación de bits real usando bytearray a menos que realmente lo desee.
 La forma más fácil de crear la tabla de código en Python es usar el tipo de datos dictionary (dict). 
 Si no le resulta familiar, es esencialmente una matriz que se puede indexar mediante una cadena o un solo carácter. 
 Se utiliza en el módulo de BinarySearchTreeTester.py que se muestra en el listado 8-12 para asignar letras de comandos a registros de comandos.
Si elige usar una matriz indexada de enteros, puede usar la función ord() de Python para convertir un carácter en un número entero, 
pero tenga en cuenta que necesitará una matriz grande si permite caracteres Unicode arbitrarios como emojis (☺) en el mensaje."""

import heapq
from collections import defaultdict

class Nodo:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

# Paso 1: Construir el árbol de Huffman
def construir_arbol_huffman(texto):
    frecuencia = defaultdict(int)
    
    # Calcular la frecuencia de cada carácter en el texto
    for caracter in texto:
        frecuencia[caracter] += 1
    
    # Crear una cola de prioridad (min heap) para construir el árbol
    heap = [Nodo(caracter, freq) for caracter, freq in frecuencia.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        # Extraer dos nodos con la menor frecuencia
        izquierda = heapq.heappop(heap)
        derecha = heapq.heappop(heap)
        
        # Crear un nuevo nodo interno con una frecuencia igual a la suma de los dos nodos
        nuevo_nodo = Nodo(None, izquierda.frecuencia + derecha.frecuencia)
        nuevo_nodo.izquierda = izquierda
        nuevo_nodo.derecha = derecha
        
        # Volver a insertar el nuevo nodo interno en la cola
        heapq.heappush(heap, nuevo_nodo)
    
    # La cola debería contener solo un nodo, que es la raíz del árbol de Huffman
    return heap[0]

# Paso 2: Generar los códigos de Huffman
def generar_codigos_huffman(raiz, codigo="", codigos={}):
    if raiz is None:
        return codigos
    
    # Si es un nodo hoja (un carácter)
    if raiz.caracter is not None:
        codigos[raiz.caracter] = codigo
    
    # Recorrer hacia la izquierda y hacia la derecha
    generar_codigos_huffman(raiz.izquierda, codigo + "0", codigos)
    generar_codigos_huffman(raiz.derecha, codigo + "1", codigos)
    
    return codigos

# Paso 3: Codificar el texto utilizando los códigos generados
def codificar_texto(texto, codigos):
    return ''.join(codigos[caracter] for caracter in texto)

# Paso 4: Decodificar la cadena binaria de vuelta al texto original
def decodificar_texto(binario, raiz):
    texto_decodificado = []
    nodo_actual = raiz
    
    for bit in binario:
        # Recorrer el árbol basado en el bit (0 para izquierda, 1 para derecha)
        nodo_actual = nodo_actual.izquierda if bit == "0" else nodo_actual.derecha
        
        # Si es un nodo hoja, añadir el carácter al texto decodificado
        if nodo_actual.caracter is not None:
            texto_decodificado.append(nodo_actual.caracter)
            nodo_actual = raiz  # Volver al nodo raíz para continuar con la siguiente secuencia de bits
    
    return ''.join(texto_decodificado)

# Función principal
def huffman_coding(texto):
    # Construir el árbol de Huffman
    raiz = construir_arbol_huffman(texto)
    
    # Generar los códigos de Huffman
    codigos_huffman = generar_codigos_huffman(raiz)
    
    # Codificar el texto
    texto_codificado = codificar_texto(texto, codigos_huffman)
    
    # Decodificar el texto
    texto_decodificado = decodificar_texto(texto_codificado, raiz)
    
    # Mostrar resultados
    print("Texto original:", texto)
    print("Texto codificado en binario:", texto_codificado)
    print("Texto decodificado:", texto_decodificado)
    print("Número de caracteres en el mensaje original:", len(texto))
    print("Número de bits en el mensaje codificado:", len(texto_codificado))
    
    return codigos_huffman, texto_codificado, texto_decodificado

# Ejemplo de uso
texto = "hola mundo"
codigos, texto_codificado, texto_decodificado = huffman_coding(texto)

# Mostrar el árbol de Huffman si el mensaje es corto
if len(texto) <= 10:
    print("\nÁrbol de Huffman:")
    for caracter, codigo in codigos.items():
        print(f"{caracter}: {codigo}")
