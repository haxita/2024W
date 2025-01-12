import numpy as np

def load_grid_from_file(filename: str) -> np.ndarray:
    """
    Loads a saved grid from the relative path filename.
    Each line represents one row, with '0's and '1's 
    indicating dead and live cells, respectively.
    
    :param filename: The path of the file to read from.
    :return: A 2D numpy array of integers (0s and 1s).
    """
    grid_list = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            # Each row is a string of '0' and '1' (possibly with spaces).
            # Split out non-digit characters if necessary:
            # e.g. if line has '0 0 1 0', we do:
            # row_values = [int(x) for x in line.split()]
            # if the file has no spaces, e.g. '0010', we can parse directly:
            
            # Attempt a robust approach: if there are spaces, use split(),
            # otherwise interpret the line as a direct string of 0s and 1s.
            if ' ' in line:
                row_values = [int(x) for x in line.split()]
            else:
                row_values = [int(char) for char in line]

            grid_list.append(row_values)

    return np.array(grid_list)

def save_grid_to_file(grid: np.ndarray, filename: str) -> None:
    """
    Saves a given grid (2D numpy array of 0s and 1s) to the path filename.
    Each row is written as 0s and 1s separated by spaces.
    
    :param grid: A 2D numpy array representing the Game of Life grid.
    :param filename: The path of the file to write to.
    """
    with open(filename, 'w') as file:
        rows, cols = grid.shape
        for r in range(rows):
            # Convert each row to a string of '0 1 0 1...' or '0 1 0...' etc.
            row_str = ''.join(str(int(cell)) for cell in grid[r])
            file.write(row_str + '\n')


# Example usage (uncomment to test within this file):
if __name__ == "__main__":
    # Suppose we have an existing text file 'initial_grid.txt' in the same folder
    my_grid = load_grid_from_file("initial_grid.txt")
    print("Loaded grid shape:", my_grid.shape)
    print(my_grid)

    # Save it to a new file
    save_grid_to_file(my_grid, "copy_of_initial.txt")

    # Print out the newly saved file's contents
    check_grid = load_grid_from_file("copy_of_initial.txt")
    print("Re-loaded grid shape:", check_grid.shape)
    print(check_grid)