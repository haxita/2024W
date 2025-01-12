import numpy as np
from a11_ex1 import count_neighbours

def apply_rules(grid: np.ndarray) -> np.ndarray:
    """
    Generates the next state of the grid according to Conway's Game of Life rules:
      1. Any live cell with fewer than two live neighbours dies (underpopulation).
      2. Any live cell with two or three live neighbours survives.
      3. Any live cell with more than three live neighbours dies (overpopulation).
      4. Any dead cell with exactly three live neighbours becomes alive (reproduction).
    """
    rows, cols = grid.shape
    new_grid = np.copy(grid)

    for r in range(rows):
        for c in range(cols):
            alive_neighbours = count_neighbours(grid, r, c)
            if grid[r, c] == 1:  # currently alive
                if alive_neighbours < 2 or alive_neighbours > 3:
                    new_grid[r, c] = 0
                else:
                    new_grid[r, c] = 1
            else:  # currently dead
                if alive_neighbours == 3:
                    new_grid[r, c] = 1
                else:
                    new_grid[r, c] = 0

    return new_grid

# Example usage (uncomment to test within this file):
if __name__ == "__main__":
    from a11_ex1 import print_grid

    grid = np.array([
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0]
    ])
    print_grid(grid)
    new_grid = apply_rules(grid)
    print_grid(new_grid)