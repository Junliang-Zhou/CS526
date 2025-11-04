def is_right_triangle(p1, p2, p3):
    def dot(u, v):
        return u[0]*v[0] + u[1]*v[1]

    AB = (p2[0] - p1[0], p2[1] - p1[1])
    AC = (p3[0] - p1[0], p3[1] - p1[1])
    BC = (p3[0] - p2[0], p3[1] - p2[1])

    return (
        dot(AB, AC) == 0 or
        dot(AB, BC) == 0 or
        dot(AC, BC) == 0
    )

with open('rightangles_3.txt', 'r') as f:
    lines = f.read().splitlines()

n = int(lines[0])
points = [tuple(map(int, line.split())) for line in lines[1:]]

count = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if is_right_triangle(points[i], points[j], points[k]):
                count += 1

print(f"The number of right triangles is: {count}")
