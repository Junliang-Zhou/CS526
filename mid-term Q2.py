def read_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    size = int(lines[0])
    infected_coords = [tuple(map(int, line.split())) for line in lines[1:]]
    return size, infected_coords

def get_neighbors(r, c, size):
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < size and 0 <= nc < size:
            yield nr, nc

def simulate_infection(size, infected_coords):
    grid = [[False for _ in range(size)] for _ in range(size)]
    for r, c in infected_coords:
        grid[r-1][c-1] = True

    changed = True
    while changed:
        changed = False
        new_grid = [row[:] for row in grid]
        for r in range(size):
            for c in range(size):
                if not grid[r][c]:
                    infected_neighbors = sum(grid[nr][nc] for nr, nc in get_neighbors(r, c, size))
                    if infected_neighbors >= 2:
                        new_grid[r][c] = True
                        changed = True
        grid = new_grid

    for row in grid:
        if not all(row):
            return "There are healthy counties left"
    return "There are no healthy counties left"

def main():
    filename = "pandemic_input2.txt"  # Change to pandemic_input2.txt to test other case
    size, infected_coords = read_input(filename)
    result = simulate_infection(size, infected_coords)
    print(result)

if __name__ == "__main__":
    main()
