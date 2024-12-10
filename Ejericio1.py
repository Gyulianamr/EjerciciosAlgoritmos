X=int(input("Cuantos numeros quiere sumar?"))
num=[]
suma=0

for i in range (X):
    Numero=int(input(f"{i+1} Ingrese un numero: "))
    num.append(Numero)

suma=sum(num)
print("el arreglo es", num)
print("la suma es:", suma)