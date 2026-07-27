# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def get_matrix(rows, cols, label=""):
    matrix = []
    print(f"\nEntering {label} matrix ({rows}x{cols}):")
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i+1}: ").split()
            if len(row_input) == cols:
                matrix.append([int(x) for x in row_input])
                break
            print(f"Error: Row must contain exactly {cols} values.")
    return matrix

def display_matrix(matrix, title="Matrix:"):
    print(f"\n{title}")
    for row in matrix:
        print("  ".join(f"{val:3d}" for val in row))

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix)
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1)
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix1[i][j] + matrix2[i][j])
        result.append(new_row)
    return result

def multiply_matrices(matA, matB):
    m = len(matA)
    n = len(matA)
    p = len(matB)
    result = []
    for i in range(m):
        new_row = []
        for j in range(p):
            total = 0
            for k in range(n):
                total += matA[i][k] * matB[k][j]
            new_row.append(total)
        result.append(new_row)
    return result

if __name__ == "__main__":
    print("--- PART A: Transpose ---")
    r1 = int(input("Enter number of rows: "))
    c1 = int(input("Enter number of columns: "))
    matA = get_matrix(r1, c1, "A")
    display_matrix(matA, "Original Matrix:")
    display_matrix(transpose_matrix(matA), "Transposed Matrix:")

    print("\n--- PART B: Addition ---")
    r2 = int(input("Enter number of rows: "))
    c2 = int(input("Enter number of columns: "))
    m1 = get_matrix(r2, c2, "Matrix 1")
    m2 = get_matrix(r2, c2, "Matrix 2")
    display_matrix(add_matrices(m1, m2), "Result of Addition:")

    print("\n--- PART C: Multiplication ---")
    ra = int(input("Enter rows for Matrix A: "))
    ca = int(input("Enter columns for Matrix A: "))
    cb = int(input("Enter columns for Matrix B: "))
    matrix_A = get_matrix(ra, ca, "A")
    matrix_B = get_matrix(ca, cb, "B")
    display_matrix(multiply_matrices(matrix_A, matrix_B), "Result of Multiplication:")
