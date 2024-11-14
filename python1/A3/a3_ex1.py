print('Number of rows: ', end='')
rows_input = input()
rows = int(rows_input)

# Prompt the user for the number of columns
print('Number of cols: ', end='')
cols_input = input()
cols = int(cols_input)

# Create the matrix with 'X' and 'O' based on the sum of indices
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        if (i + j) % 2 == 0:
            row.append('X')
        else:
            row.append('O')
    matrix.append(row)

# Print the header with column indices without trailing space
print('    ', end='')
for j in range(cols):
    if j < cols - 1:
        print(j, end=' ')
    else:
        print(j, end='')
print()

# Print the separator line
separator_length = cols * 2 + 1
print('   ' + '-' * separator_length)

# Print each row with row index and matrix elements
for i in range(rows):
    print(f"{i} |", end=' ')
    for elem in matrix[i]:
        print(elem, end=' ')
    print('|')

# Print the bottom separator line
print('   ' + '-' * separator_length)