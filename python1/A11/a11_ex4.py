import time

import numpy as np
from a11_ex1 import create_grid, print_grid, number_of_live_cells
from a11_ex1 import count_neighbours  # might not be necessary here
from a11_ex2 import apply_rules
from a11_ex3 import load_grid_from_file, save_grid_to_file

def main():
    print("Welcome to the Game of Life!")
    choice = input("Load initial state from file? (y/n): ").strip().lower()

    if choice == 'y':
        filename = input("Enter filename: ").strip()
        grid = load_grid_from_file(filename)
    else:
        # random creation
        rows_cols = input("Enter number of rows and columns, separated by a space: ").strip()
        r, c = rows_cols.split()
        r, c = int(r), int(c)
        grid = create_grid(r, c)

    # Print the initial grid
    print_grid(grid)
    generation = 0

    # We will run the game in chunks of 10 generations,
    # with the user prompted after each chunk
    while True:
        # Run for 10 generations
        for _ in range(10):
            # Print the current generation number and the number of live cells
            print(f"Generation {generation}, live cells: {number_of_live_cells(grid)}")
            # Evolve the grid by 1 generation
            grid = apply_rules(grid)
            # Optionally print the new grid:
            # print_grid(grid)
            generation += 1
            
            # (Optional) Sleep for a fraction of a second to slow things down
            # time.sleep(0.1)

        # After 10 generations, ask user
        user_input = input("Press ENTER to continue,'s' to save, or 'q' to quit: ").strip().lower()

        if user_input == 'q':
            break
        elif user_input == 's':
            save_filename = input("Enter filename to save: ").strip()
            save_grid_to_file(grid, save_filename)
            # After saving, we continue the loop for another set of 10 gens
            # So do nothing else here
        else:
            # If user just pressed ENTER, continue another 10 generations
            pass

    # Final message if you want:
    print("Goodbye!")

# If this file is run directly, call main()
if __name__ == "__main__":
    main()