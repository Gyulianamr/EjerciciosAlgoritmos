#9.	Pila de Números Simula una calculadora que use una pila para realizar operaciones básicas (+, -, *, /). Los números y operaciones se ingresan como una lista.
#

class Calculadora:
    def __init__(self):
     
        self.__pila = []

    def Push(self, numero):
       
        self.__pila.append(numero)

    def realizar_operacion(self, operador):
       
        if len(self.__pila) < 2:
            raise ValueError("No hay suficientes operandos en la pila para realizar la operación.")

        
        b = self.__pila.pop()
        a = self.__pila.pop()

    
        if operador == '+':
            resultado = a + b
        elif operador == '-':
            resultado = a - b
        elif operador == '*':
            resultado = a * b
        elif operador == '/':
            if b == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            resultado = a / b
        else:
            raise ValueError(f"Operador no válido: {operador}")

        self.__pila.append(resultado)

    def obtener_resultado(self):
        if not self.__pila:
            raise ValueError("La pila está vacía. No hay resultado para mostrar.")

  
        return self.__pila[-1]


calc = Calculadora()

   
entrada = [5, 3, '+', 2, '*', 10, '/']

for elemento in entrada:
    if isinstance(elemento, (int, float)):
        calc.Push(elemento)
    elif isinstance(elemento, str):
        calc.realizar_operacion(elemento)
    else:
        raise ValueError(f"Elemento no reconocido: {elemento}")

resultado = calc.obtener_resultado()
print(f"El resultado es: {resultado}")
