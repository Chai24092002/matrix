def get_matrix(rows, cols, name):
    print(f"Enter elements for {name} matrix:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            print("Error: Please enter the correct number of elements.")
            return get_matrix(rows, cols, name)
        matrix.append(row)
    return matrix

def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    if cols_A != rows_B:
        print("Matrix multiplication is not possible. Columns of A must equal rows of B.")
        return None
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def print_matrix(matrix, name):
    print(f"{name} Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    rows_A = int(input("Enter number of rows for Matrix A: "))
    cols_A = int(input("Enter number of columns for Matrix A: "))
    A = get_matrix(rows_A, cols_A, "A")
    
    rows_B = int(input("Enter number of rows for Matrix B: "))
    cols_B = int(input("Enter number of columns for Matrix B: "))
    B = get_matrix(rows_B, cols_B, "B")
    
    result = multiply_matrices(A, B)
    
    if result:
        print_matrix(A, "Matrix A")
        print_matrix(B, "Matrix B")
        print_matrix(result, "Result")

if __name__ == "__main__":
    main()

