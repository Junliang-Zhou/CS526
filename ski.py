import sys
sys.setrecursionlimit(10000)

# Read input file
with open(sys.argv[1], 'r') as f:
    lines = f.read().strip().split('\n')

rows = int(lines[0])
cols = int(lines[1])
grid = [list(map(int, line.split())) for line in lines[2:]]

# 8 directions: N, NE, E, SE, S, SW, W, NW
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
              (1, 0), (1, -1), (0, -1), (-1, -1)]

memo = [[-1 for _ in range(cols)] for _ in range(rows)]

def dfs(r, c):
    if memo[r][c] != -1:
        return memo[r][c]
    
    max_len = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] < grid[r][c]:
            max_len = max(max_len, 1 + dfs(nr, nc))
    
    memo[r][c] = max_len
    return max_len

longest = 0
for i in range(rows):
    for j in range(cols):
        longest = max(longest, dfs(i, j))

print(longest)

