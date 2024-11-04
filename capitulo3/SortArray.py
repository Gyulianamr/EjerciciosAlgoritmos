# Implement a sortable Array data structure

class Array(object):
   def __init__(self, initialSize):    # Constructor
      self.__a = [None] * initialSize  # The array stored as a list
      self.__nItems = 0                # No items in array initially
      self._capacity = initialSize 
   def __len__(self):                  # Special def for len() func
      return self.__nItems             # Return number of items

   def __getitem__(self, index):       # Allow access via arr[index]
      if 0 <= index < self.__nItems:
         return self.__a[index]
      else:
         raise IndexError("Index out of range")

   def __setitem__(self, index, value): # Allow setting via arr[index]
      if 0 <= index < self.__nItems:
         self.__a[index] = value
      else:
         raise IndexError("Index out of range")

   def get(self, n):                   # Return the value at index n
      if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
         return self.__a[n]            # only return item if in bounds
   
   def set(self, n, value):            # Set the value at index n
      if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
         self.__a[n] = value           # only set item if in bounds

   def swap(self, j, k):               # Swap the values at 2 indices
      if (0 <= j and j < self.__nItems and # Check if indices are in
          0 <= k and k < self.__nItems): # bounds, before processing
         self.__a[j], self.__a[k] = self.__a[k], self.__a[j]
         
   def insert(self, item):             # Insert item at end
      if self.__nItems >= len(self.__a): # If array is full,
         raise Exception("Array overflow") # raise exception
      self.__a[self.__nItems] = item   # Item goes at current end
      self.__nItems += 1               # Increment number of items

   def find(self, item):               # Find index for item
      for j in range(self.__nItems):   # Among current items
         if self.__a[j] == item:       # If found,
            return j                   # then return index to item
      return -1                        # Not found -> return -1
   
   def search(self, item):             # Search for item
      return self.get(self.find(item)) # and return item if found

   def delete(self, item):             # Delete first occurrence
      for j in range(self.__nItems):   # of an item
         if self.__a[j] == item:       # Found item
            self.__nItems -= 1         # One fewer at end
            for k in range(j, self.__nItems):  # Move items from
               self.__a[k] = self.__a[k+1]     # right over 1
            return True                # Return success flag
      
      return False     # Made it here, so couldn't find the item
   
   def deleteLast(self, n=1):          # Delete last n items
      for j in range(min(n, self.__nItems)): # n defaults to 1
         self.__nItems -= 1            # Decrease number of items
         self.__a[self.__nItems] = None # Free up any space taken
         
   def traverse(self, function=print): # Traverse all items
      for j in range(self.__nItems):   # and apply a function
         function(self.__a[j])

   def __str__(self):                  # Special def for str() func
      ans = "["                        # Surround with square brackets
      for i in range(self.__nItems):   # Loop through items
         if len(ans) > 1:              # Except next to left bracket,
            ans += ", "                # separate items with comma
         ans += str(self.__a[i])       # Add string form of item
      ans += "]"                       # Close with right bracket
      return ans

   def bubbleSort(self):               # Sort comparing adjacent vals
      for last in range(self.__nItems-1, 0, -1):  # and bubble up
         for inner in range(last):     # inner loop goes up to last
            if self.__a[inner] > self.__a[inner+1]:  # If item less
               self.swap(inner, inner+1) # than adjacent item, swap
               
   def selectionSort(self):           # Sort by selecting min and 
      for outer in range(self.__nItems-1): # swapping min to leftmost
         min = outer                  # Assume min is leftmost
         for inner in range(outer+1, self.__nItems): # Hunt to right
            if self.__a[inner] < self.__a[min]: # If we find new min,
               min = inner            # update the min index
               
         # __a[min] is smallest among __a[outer]...__a[__nItems-1]
         self.swap(outer, min)        # Swap leftmost and min
   
   #3.5 modificacion 
   def insertionSort(self):
       total_copias = 0  # Total copies across all passes
       total_comparaciones = 0  # Total comparisons across all passes

       for outer in range(1, self.__nItems):  # Mark one item
           temp = self.__a[outer]  # Store marked item in temp
           inner = outer  # Inner loop starts at mark
           
           copias = 0  # Initialize copy count for this pass
           comparaciones = 0  # Initialize comparison count for this pass
           
           while inner > 0:
               comparaciones += 1  # Increment comparison count
               if temp < self.__a[inner - 1]:  # If marked item is smaller
                   self.__a[inner] = self.__a[inner - 1]  # Shift item to right
                   inner -= 1  # Move to the left
                   copias += 1  # Increment copy count
               else:
                   break  # No more comparisons needed
           
           self.__a[inner] = temp  # Move marked item to 'hole'
           copias += 1  # Increment copy count for placing the temp
           
           # Update total counts
           total_copias += copias
           total_comparaciones += comparaciones

       return total_copias, total_comparaciones  # Return the totals for printing

   

 #3.1
   def Bidireccionalburb(arr):
      n = len(arr)
      swapped = True
      start = 0
      end = n - 1

      while swapped:
         swapped = False
         
         # De izquierda a derecha
         for i in range(start, end):
               if arr[i] > arr[i + 1]:
                  arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Intercambiar
                  swapped = True
         
         # Si no se realizaron intercambios, el arreglo está ordenado
         if not swapped:
               break
         
         end -= 1
         swapped = False
         
         # De derecha a izquierda
         for i in range(end, start, -1):
               if arr[i] < arr[i - 1]:
                  arr[i], arr[i - 1] = arr[i - 1], arr[i]  # Intercambiar
                  swapped = True
         
         # Aumenta el rango del inicio porque el primer elemento ya está en su lugar
         start += 1

      return arr

#3.2
   def median(self):
      
      self.bubbleSort()  

      if self.__nItems == 0:
         raise ValueError("Cannot compute median of an empty array")

      mid = self.__nItems // 2 

      if self.__nItems % 2 == 1:
      
         return self.__a[mid]
      else:
        
         return (self.__a[mid - 1] + self.__a[mid]) / 2

   #3.3

   def deduplicate(self):
      if self.__nItems <= 1:
               return  
      self.bubbleSort()  
      lastUniqueIndex = 0


      for i in range(1, self.__nItems):
         if self.__a[i] != self.__a[lastUniqueIndex]:  # Si encontramos un valor único
               lastUniqueIndex += 1                     # Mover el índice a la siguiente posición única
               self.__a[lastUniqueIndex] = self.__a[i]  
      self.__nItems = lastUniqueIndex + 1  # Solo los elementos únicos se mantienen en el array
      
      # Opcional: Limpiar el resto del array
      for i in range(self.__nItems, len(self.__a)):
         self.__a[i] = None

   def swap(self, j, k):
      if (0 <= j < self.__nItems and  # Verificamos que j esté en rango
         0 <= k < self.__nItems):    # Verificamos que k esté en rango
         self.__a[j], self.__a[k] = self.__a[k], self.__a[j]  # Realizamos el intercambio

         
#3.4

   def oddEvenSort(self):
      n = self.__nItems
      sorted = False  # Inicializa como no ordenado
      passes = 0      # Contador de pasadas

      while not sorted:  # Bucle hasta que el array esté ordenado
         sorted = True   # Asumimos que está ordenado al inicio de cada pasada

         # Paso 1: Comparar e intercambiar elementos en posiciones impares
         for j in range(1, n - 1, 2):  # j = 1, 3, 5, ...
               if self.__a[j] > self.__a[j + 1]:  # Comparar elementos
                  self.swap(j, j + 1)  # Realizar intercambio
                  sorted = False  # Si hay un intercambio, no está ordenado

         # Paso 2: Comparar e intercambiar elementos en posiciones pares
         for j in range(0, n - 1, 2):  # j = 0, 2, 4, ...
               if self.__a[j] > self.__a[j + 1]:  # Comparar elementos
                  self.swap(j, j + 1)  # Realizar intercambio
                  sorted = False  # Si hay un intercambio, no está ordenado

         passes += 1  # Incrementar el contador de pasadas

      return passes  # Retornar el número total de pasadas realizadas

#3.6

   def insertionSortAndDedupe(self, low_value=float('-inf')):
      """Sorts the array and removes duplicates."""
      duplicates_count = 0  # Count of duplicates found
      for outer in range(1, self.__nItems):
         temp = self.__a[outer]
         inner = outer
         while inner > 0:
               if temp < self.__a[inner - 1]:
                  self.__a[inner] = self.__a[inner - 1]
               elif temp == self.__a[inner - 1]:
                  duplicates_count += 1  # Count duplicates
                  self.__a[outer] = low_value  # Replace with low value
                  break
               else:
                  break
               inner -= 1
         
         if self.__a[outer] != low_value:  # Only insert if it's not a duplicate
               self.__a[inner] = temp

      # Move unique elements to the front of the array
      unique_index = 0
      for i in range(self.__nItems):
         if self.__a[i] != low_value:
               self.__a[unique_index] = self.__a[i]
               unique_index += 1

      self.__nItems = unique_index  # Update the number of items
      for i in range(unique_index, self._capacity):  # Accessing the mangled name
         self.__a[i] = None  # Updated to clear remaining elements
