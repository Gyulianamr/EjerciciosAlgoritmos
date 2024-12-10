#8.	Revertir una Cadena con una Pila Escribe una función que use una pila para invertir una cadena de texto#

def Invertircadena(cadena):
    pila=[]
    for char in cadena:
        pila.append(char)
        cadenainvertida= ""
    while pila:
            cadenainvertida += pila.pop()
        
    return cadenainvertida

    


# Ejemplo de uso
cadena1 = "{hola}"
cadena2 = "{Adios}"
print(Invertircadena(cadena1))  
print(Invertircadena(cadena2))  

