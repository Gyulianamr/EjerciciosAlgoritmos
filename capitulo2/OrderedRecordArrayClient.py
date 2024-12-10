from OrderedRecordArray import OrderedRecordArray

def second(x):  # Key on second element of record
    return x[1]

maxSize = 1000  # Max size of the array
arr = OrderedRecordArray(maxSize, second)  # Create the array object

# Insert 10 items
for rec in [('a', 3.1), ('b', 7.5), ('c', 6.0), ('d', 3.1),
            ('e', 1.4), ('f', -1.2), ('g', 0.0), ('h', 7.5),
            ('i', 7.5), ('j', 6.0)]:
    arr.insert(rec)

print("Array containing", len(arr), "items:\n", arr)

# Delete a few items, including some duplicates
to_delete = [('c', 6.0), ('g', 0.0), ('g', 0.0), 
             ('b', 7.5), ('i', 7.5)]

for rec in to_delete:
    result = arr.remove(rec)  
    print("Deleting", rec, "returns", result)

print("Array after deletions has", len(arr), "items:\n", arr)

# Verificar si los elementos restantes son correctos
remaining_keys = [1.4, 3.1, -1.2, 7.5, 6.0]  # Claves que deberían quedar
for key in remaining_keys:
    index = arr.find(key)
    if index != -1:
        print("find(", key, ") returns", index,
              "and get(", index, ") returns", arr.get(index))
    else:
        print("find(", key, ") returns", "Key not found")

