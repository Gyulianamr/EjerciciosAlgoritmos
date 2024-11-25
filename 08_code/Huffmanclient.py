from Huffman import build_huffman_tree, build_code_table, encode_message, decode_message, display_huffman_tree

text = "Hola"
huffman_tree = build_huffman_tree(text)
code_table = build_code_table(huffman_tree)
encoded_message = encode_message(text, code_table)
decoded_message = decode_message(encoded_message, huffman_tree)

print("Huffman Code Table:", code_table)
print("Encoded Message:", encoded_message)
print("Decoded Message:", decoded_message)
print("\nHuffman Tree:")
display_huffman_tree(huffman_tree)

