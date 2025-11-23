def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]; j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]; j -= 1
        arr[j+1] = key
    return arr

def read_input_file(filename):
    try:
        with open(filename, 'r') as f:
            return list(map(int, f.read().strip().split()))
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return []

for fname in ["HW6 Q1 Small Input.txt", "HW6 Q1 Medium Input.txt", "HW6 Q1 Large Input.txt"]:
    print(f"\n File: {fname}")
    data = read_input_file(fname)
    if not data: continue
    print("Original:", data)
    print("Sorted (Insertion Sort):", insertion_sort(data))
