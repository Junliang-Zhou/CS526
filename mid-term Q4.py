def main():
    filename = "spg_input2.txt"  # Change to spg_input2.txt to test other case
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    n = int(lines[0])
    symbols = set(lines[1].split(','))
    board = [row.split(',') for row in lines[2:]]

    sqrt_n = int(n ** 0.5)

    # Check rows
    for row in board:
        seen = set()
        for cell in row:
            if cell == '.':
                continue
            if cell not in symbols or cell in seen:
                print("The board is invalid")
                return
            seen.add(cell)

    # Check columns
    for col in range(n):
        seen = set()
        for row in range(n):
            cell = board[row][col]
            if cell == '.':
                continue
            if cell not in symbols or cell in seen:
                print("The board is invalid")
                return
            seen.add(cell)

    # Check sub-boards
    for box_row in range(0, n, sqrt_n):
        for box_col in range(0, n, sqrt_n):
            seen = set()
            for r in range(box_row, box_row + sqrt_n):
                for c in range(box_col, box_col + sqrt_n):
                    cell = board[r][c]
                    if cell == '.':
                        continue
                    if cell not in symbols or cell in seen:
                        print("The board is invalid")
                        return
                    seen.add(cell)

    print("The board is valid")

if __name__ == "__main__":
    main()
