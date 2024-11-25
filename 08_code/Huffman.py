import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    if not text:
        return None
    
    freq = Counter(text)
    priority_queue = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)
    
    return priority_queue[0]

def build_code_table(node, code="", code_table=None):
    if code_table is None:
        code_table = {}
    
    if node:
        if node.char is not None:
            code_table[node.char] = code
        build_code_table(node.left, code + "0", code_table)
        build_code_table(node.right, code + "1", code_table)
    
    return code_table

def encode_message(message, code_table):
    return ''.join(code_table[char] for char in message)

def decode_message(binary_message, huffman_tree):
    decoded_text = []
    node = huffman_tree
    
    for bit in binary_message:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            decoded_text.append(node.char)
            node = huffman_tree
    
    return ''.join(decoded_text)

def display_huffman_tree(node, level=0):
    if node:
        display_huffman_tree(node.right, level + 1)
        print("   " * level + (f"'{node.char}'" if node.char else "•"))
        display_huffman_tree(node.left, level + 1)

