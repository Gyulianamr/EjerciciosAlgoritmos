class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def insert_left(self, item):
        if self.is_full():
            raise Exception("Deque is full")
        self.front = (self.front - 1) % self.capacity
        self.items[self.front] = item
        self.size += 1

    def insert_right(self, item):
        if self.is_full():
            raise Exception("Deque is full")
        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def remove_left(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        item = self.items[self.front]
        self.items[self.front] = None  # Optional: clear the reference
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def remove_right(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        self.rear = (self.rear - 1) % self.capacity
        item = self.items[self.rear]
        self.items[self.rear] = None  # Optional: clear the reference
        self.size -= 1
        return item

    def peek_left(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.items[self.front]

    def peek_right(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.items[(self.rear - 1) % self.capacity]

#4.4
class Stack:
    def __init__(self, capacity):
        self.deque = Deque(capacity)

    def is_empty(self):
        return self.deque.is_empty()

    def is_full(self):
        return self.deque.is_full()

    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full")
        self.deque.insert_right(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.deque.remove_right()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.deque.peek_right()


if __name__ == "__main__":
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    print(stack.peek())  # Output: 2
    print(stack.pop())   # Output: 2
    print(stack.is_empty())  # Output: False

