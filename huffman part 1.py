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

def build_frequency_map(text):
    freq_map = Counter(text)
    print("Frequency Map:", dict(freq_map))
    return freq_map

def build_huffman_tree(freq_map):
    heap = [Node(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]

def build_codes(node, prefix="", code_map={}):
    if node is None:
        return
    if node.char is not None:
        code_map[node.char] = prefix
    build_codes(node.left, prefix + "0", code_map)
    build_codes(node.right, prefix + "1", code_map)
    return code_map

def compress(text, code_map):
    return ''.join(code_map[char] for char in text)

def save_compressed(compressed, code_map):
    with open("compressed.txt", "w") as f:
        f.write(compressed)
    with open("codes.txt", "w") as f:
        for char, code in code_map.items():
            f.write(f"{char}:{code}\n")

def main():
    text = "Happy Christmas"
    print("Input Text:", text)
    freq_map = build_frequency_map(text)
    root = build_huffman_tree(freq_map)
    code_map = build_codes(root)
    print("Huffman Codes:", code_map)
    compressed = compress(text, code_map)
    print("Compressed Binary:", compressed)
    save_compressed(compressed, code_map)

if __name__ == "__main__":
    main()
