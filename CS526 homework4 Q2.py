# Replace 'smallest_input.txt' with your actual filename
with open('fewest_3.txt', 'r') as file:
    lines = file.read().splitlines()

n = int(lines[0])
target = int(lines[1])
array = list(map(int, lines[2].split()))


array.sort(reverse=True)

current_sum = 0
count = 0

for num in array:
    current_sum += num
    count += 1
    if current_sum > target:
        break

print(f"Input: {','.join(map(str, array))} Target: {target} Answer: {count}")
