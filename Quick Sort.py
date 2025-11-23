def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

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
    print("Sorted (Quick Sort):", quick_sort(data))
