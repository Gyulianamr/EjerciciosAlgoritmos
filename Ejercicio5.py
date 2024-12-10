#5.	Eliminar Duplicados Crea una función que elimine los valores duplicados de un arreglo y devuelva un nuevo arreglo con valores únicos.
#


def duplicados(num): 
    unicos= []  
    
    for elem in num: 
        existe=False
        for com in unicos:
            if com==elem:
                existe= True
                break

        if not existe:
            unicos.append(elem)

        
    return unicos
            
    
    






mi_arreglo = [1, 2, 3, 4, 5,5, 1, 4]
duplicados= duplicados(mi_arreglo)
print("sin duplicados:", duplicados)