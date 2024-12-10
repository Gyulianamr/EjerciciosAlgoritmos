###3.	Invertir un Arreglo Crea una función que reciba un arreglo y devuelva un nuevo arreglo con los elementos en orden inverso.###

def invertir_arreglo(num):
    arr = num  
    posicion = []  
    
    for i in range(len(arr) - 1, -1, -1): 
        posicion.append(arr[i])  
    
    return posicion  







#
mi_arreglo = [1, 2, 3, 4, 5]
arreglo_invertido = invertir_arreglo(mi_arreglo)
print("Arreglo invertido:", arreglo_invertido)
