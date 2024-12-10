#7.	Verificar Paréntesis Balanceados Usa una pila para verificar si una cadena de paréntesis ((), {}, []) está balanceada.#
def esta_balanceada(cadena):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}  

    for char in cadena:
        if char in "([{":  pila.append(char)
        elif char in ")]}":  
            if not pila or pila[-1] != pares[char]:
                return False 
            pila.pop() 
    return not pila  



cadena1 = "{[()()]}"  
cadena2 = "{[(])}"    
print(esta_balanceada(cadena1))  
print(esta_balanceada(cadena2))  
