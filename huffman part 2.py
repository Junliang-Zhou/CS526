def load_codes():
    code_map = {}
    with open("codes.txt", "r") as f:
        for line in f:
            char, code = line.strip().split(":")
            code_map[code] = char
    return code_map

def decompress(binary, code_map):
    current = ""
    result = ""
    for bit in binary:
        current += bit
        if current in code_map:
            result += code_map[current]
            current = ""
    return result

def main():
    with open("compressed.txt", "r") as f:
        binary = f.read()
    print("Compressed Input:", binary)
    code_map = load_codes()
    text = decompress(binary, code_map)
    print("Reconstructed Text:", text)
    with open("reconstructed.txt", "w") as f:
        f.write(text)

if __name__ == "__main__":
    main()
