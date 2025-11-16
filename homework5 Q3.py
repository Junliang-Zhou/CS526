def read_input(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        m = int(f.readline())
        A = list(map(int, f.readline().split()))
        B = list(map(int, f.readline().split()))
    return A, B

def longest_alternating_increasing(A, B):
    def build(A, B):
        n, m = len(A), len(B)
        dpA = [[] for _ in range(n)]
        dpB = [[] for _ in range(m)]

        for i in range(n):
            dpA[i] = [A[i]]
            for j in range(i):
                if A[j] < A[i] and len(dpA[j]) + 1 > len(dpA[i]):
                    dpA[i] = dpA[j] + [A[i]]

        for i in range(m):
            dpB[i] = [B[i]]
            for j in range(i):
                if B[j] < B[i] and len(dpB[j]) + 1 > len(dpB[i]):
                    dpB[i] = dpB[j] + [B[i]]

        best = []

        for i in range(n):
            for j in range(m):
                if A[i] < B[j]:
                    seq = [A[i]] + dpB[j]
                    if len(seq) > len(best):
                        best = seq
                if B[j] < A[i]:
                    seq = [B[j]] + dpA[i]
                    if len(seq) > len(best):
                        best = seq
        return best

    return max(build(A, B), build(B, A), key=len)

def main():
    input_file = "longest_seq1.txt"
    A, B = read_input(input_file)
    result = longest_alternating_increasing(A, B)
    print(f"File Input: {input_file}")
    print(f"Longest Sequence: {len(result)}")

if __name__ == "__main__":
    main()
















