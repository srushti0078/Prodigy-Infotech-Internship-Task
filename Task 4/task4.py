def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None, None

def is_valid_move(grid, row, col, num):
    return (
        all(num != grid[row][i] for i in range(9)) and
        all(num != grid[i][col] for i in range(9)) and
        all(
            num != grid[row//3*3 + i][col//3*3 + j]
            for i in range(3) for j in range(3)
        )
    )

def solve_sudoku(grid):
    row, col = find_empty_location(grid)

    if row is None and col is None:
        return True

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0

    return False

# Example unsolved Sudoku puzzle
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Unsolved Sudoku puzzle:")
print_grid(grid)

if solve_sudoku(grid):
    print("\nSolved Sudoku puzzle:")
    print_grid(grid)
else:
    print("\nNo solution exists.")
