import numpy as np

def create_grid(rows: int, cols: int) -> np.ndarray:
    """
    Creates and returns a randomly generated 2D numpy array of 0s and 1s.
    Uses np.random.seed(0) to ensure reproducibility.
    """
    np.random.seed(0)  # set seed for reproducible results
    grid = np.random.randint(0, 2, size=(rows, cols))
    return grid

def count_neighbours(grid: np.ndarray, row: int, col: int) -> int:
    """
    Counts the number of alive neighbours (cells with value 1)
    around the cell at index [row, col].
    """
    rows, cols = grid.shape
    neighbour_positions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    count = 0
    for dr, dc in neighbour_positions:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols:
            count += grid[r, c]
    return count

def print_grid(grid: np.ndarray) -> None:
    """
    Prints the grid to the console as a table with '*' for live cells (1)
    and '.' for dead cells (0).
    Adds an empty line after printing the grid.
    """
    for row in grid:
        row_str = "".join("*" if cell == 1 else "." for cell in row)
        # Alternatively, you could insert spaces, e.g.: " ".join(...)
        print(" ".join(row_str))
    print()  # empty line after the grid

def number_of_live_cells(grid: np.ndarray) -> int:
    """
    Returns the total number of live cells in the grid.
    """
    return int(np.sum(grid))

#Example usage:
if __name__ == "__main__":
    my_grid = create_grid(5, 5)
    print_grid(my_grid)
    print(number_of_live_cells(my_grid))
    print(count_neighbours(my_grid, 0, 0))
    print(count_neighbours(my_grid, 2, 2))
    print(count_neighbours(my_grid, 4, 4))
    print(count_neighbours(my_grid, 0, 4))