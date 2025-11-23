def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: result.append(left[i]); i += 1
        else: result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result

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
    print("Sorted (Merge Sort):", merge_sort(data))





