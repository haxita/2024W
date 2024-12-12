import numpy as np

def matrix_operations(size: int) -> tuple[np.ndarray, np.ndarray, int, tuple[int, int, int], tuple[int, int, int], int, np.ndarray]:
    # Check that the input size is greater than 0
    if size <= 0:
        raise ValueError("Size must be greater than 0.")
    
    # Create the 3D matrix of shape (size, size, size) with random integers between 0 and 100
    matrix = np.random.randint(0, 101, size=(size, size, size))
    
    # Compute sums:
    # 1) Sum along axis=0 (resulting in a (size, size) array)
    axis_0_sum = np.sum(matrix, axis=0)
    
    # 2) Sum along axis=(0,1) (resulting in a (size,) array)
    axis_01_sum = np.sum(matrix, axis=(0,1))
    
    # 3) Sum of all elements (a single integer)
    axis_all_sum = np.sum(matrix)
    
    # Find the index of the highest and lowest values
    # argmax and argmin return indices in the flattened array
    max_idx_flat = np.argmax(matrix)
    min_idx_flat = np.argmin(matrix)
    
    # Convert these flattened indices to 3D indices using unravel_index
    max_index = np.unravel_index(max_idx_flat, (size, size, size))
    min_index = np.unravel_index(min_idx_flat, (size, size, size))
    
    # Compute the sum of all border values.
    # Border values are those on any face of the cube:
    # i.e., i=0 or i=size-1 OR j=0 or j=size-1 OR k=0 or k=size-1
    # One way is to directly mask these conditions.
    border_mask = (
        (np.arange(size).reshape(-1,1,1) == 0) | (np.arange(size).reshape(-1,1,1) == size-1) | 
        (np.arange(size).reshape(1,-1,1) == 0) | (np.arange(size).reshape(1,-1,1) == size-1) |
        (np.arange(size).reshape(1,1,-1) == 0) | (np.arange(size).reshape(1,1,-1) == size-1)
    )
    # Constructing the mask for each dimension:
    i, j, k = np.indices((size, size, size))
    border_condition = (i == 0) | (i == size-1) | (j == 0) | (j == size-1) | (k == 0) | (k == size-1)
    border_sum = np.sum(matrix[border_condition])
    
    # Flatten the matrix and normalize to [0, 1]
    flattened = matrix.flatten()
    max_val = flattened.max()
    if max_val > 0:
        normed_array = flattened / max_val
    else:
        # If all values are zero, normalization would lead to division by zero. 
        # In that case, just return the flattened array of zeros.
        normed_array = flattened.astype(float)
    
    # Return the results as a tuple
    return (axis_0_sum, axis_01_sum, axis_all_sum, max_index, min_index, border_sum, normed_array)


# Example usage (as given in the problem statement):
if __name__ == "__main__":
    np.random.seed(0)
    axis_0_sum, axis_01_sum, axis_all_sum, max_index, min_index, border_sum, normed_array = matrix_operations(3)
    print("Sum of elements along axis 0: \n", axis_0_sum)
    print("Sum of elements along axis 0 and 1: \n", axis_01_sum)
    print("Sum of all elements: \n", axis_all_sum)
    print("Index of maximum value: \n", max_index)
    print("Index of minimum value: \n", min_index)
    print("Sum of border values: \n", border_sum)
    print("Normalized array: \n", normed_array)

    np.random.seed(0)
    axis_0_sum, axis_01_sum, axis_all_sum, max_index, min_index, border_sum, normed_array = matrix_operations(4)
    print("\nSum of elements along axis 0: \n", axis_0_sum)
    print("Sum of elements along axis 0 and 1: \n", axis_01_sum)
    print("Sum of all elements: \n", axis_all_sum)
    print("Index of maximum value: \n", max_index)
    print("Index of minimum value: \n", min_index)
    print("Sum of border values: \n", border_sum)
    print("Normalized array: \n", normed_array)