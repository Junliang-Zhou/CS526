MORSE_VOWELS = {
    'A': '.-',
    'E': '.',
    'I': '..',
    'O': '---',
    'U': '..-'
}
VOWEL_CODES = set(MORSE_VOWELS.values())

def count_vowel_combinations(code):
    n = len(code)
    dp = [0] * (n + 1)
    dp[0] = 1  # base case: empty string

    for i in range(1, n + 1):
        for vcode in VOWEL_CODES:
            l = len(vcode)
            if i >= l and code[i - l:i] == vcode:
                dp[i] += dp[i - l]
    return dp[n]

def main(file_number):
    filename = f"vowel_input{file_number}.txt"
    with open(filename, 'r') as f:
        total = int(f.readline().strip())
        code = f.readline().strip()
        if len(code) != total:
            print(f"Warning: expected {total} symbols, got {len(code)}")

    result = count_vowel_combinations(code)
    print(f"File Input: vowel_input{file_number}.txt")
    print(f"The Number of Vowel combinations is: {result}")

if __name__ == "__main__":
    file_number = input("Enter input file number : ").strip()
    main(file_number)
