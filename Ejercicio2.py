x = [4, 0, 3, 5, 1]
menor = x[0]
mayor=x[0]

for num in x:
    if num <= menor:
        menor = num

for num in x:
    if num>=mayor:
        mayor=num


print("El menor número es:", menor)

print("El menor número es:", mayor)
