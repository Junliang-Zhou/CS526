# NOT COMPLETED
def parse_pair(pair):
    bx, by = int(pair[1]), int(pair[2])
    gx, gy = int(pair[4]), int(pair[5])
    return ((bx, by), (gx, gy))

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def read_input_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    n = int(lines[0])
    pairs = lines[1:]

result = read_input_file("ghostbusters_input.txt")
print(result)
