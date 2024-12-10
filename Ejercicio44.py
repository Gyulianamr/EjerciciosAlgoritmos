##4.	Buscar un Elemento Escribe un programa que tome un arreglo y un número, y determine si el número está presente en el arreglo.
##
def buscar_num(num, buscar):
    arr = num 
    encontrar=buscar
    
    for i in range(len(arr)): 
        if arr[i] == encontrar:
            print("El numero se encuentra en el arreglo")

            return True
        else:
            no= print(" El numero no se encuentra en el arreglo")
            
            return None
        
 







#
mi_arreglo = [1, 2, 3, 4, 5]
buscar=6
busqueda = buscar_num(mi_arreglo, buscar)
print(busqueda)