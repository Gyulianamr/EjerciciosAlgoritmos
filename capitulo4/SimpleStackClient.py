from SimpleStack import Stack, StackOverflowError, StackUnderflowError

stack = Stack(10)

for word in ['May', 'the', 'force', 'be', 'with', 'you']:
    stack.push(word)

print('After pushing', len(stack), 
      'words on the stack, it contains:\n', stack)
print('Is stack full?', stack.isFull())

print('Popping items off the stack:')
while not stack.isEmpty():
    print(stack.pop(), end=' ')
print()

print("Pushing items onto the stack:")
for i in range(len(stack)):  # Cambiado a len(stack)
    stack.push(i)
    print(f"Pushed {i}: {stack}")

# Intentar agregar otro elemento a la pila llena
try:
    print("Attempting to push onto a full stack...")
    stack.push(len(stack))  # Esto debería lanzar una excepción
except StackOverflowError as e:
    print(e)

print("\nPopping items from the stack:")
while not stack.isEmpty():
    popped_item = stack.pop()
    print(f"Popped {popped_item}: {stack}")

# Intentar quitar otro elemento de la pila vacía
try:
    print("Attempting to pop from an empty stack...")
    stack.pop()  # Esto debería lanzar una excepción
except StackUnderflowError as e:
    print(e)
