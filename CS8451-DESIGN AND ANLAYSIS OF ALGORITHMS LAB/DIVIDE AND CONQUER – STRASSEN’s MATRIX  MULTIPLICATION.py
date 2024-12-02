import numpy as np

def strassen_multiply(A, B):
    n = len(A)
    # Base case: If the matrices are 1x1, perform standard multiplication
    if n == 1:
        return np.array([[A[0][0] * B[0][0]]])
    # Split matrices into four equal-sized submatrices
    a11, a12, a21, a22 = A[:n//2, :n//2], A[:n//2, n//2:], A[n//2:, :n//2], A[n//2:, n//2:]
    b11, b12, b21, b22 = B[:n//2, :n//2], B[:n//2, n//2:], B[n//2:, :n//2], B[n//2:, n//2:]
    # Recursive computation of seven products
    p1 = strassen_multiply(a11 + a22, b11 + b22)
    p2 = strassen_multiply(a21 + a22, b11)
    p3 = strassen_multiply(a11, b12 - b22)
    p4 = strassen_multiply(a22, b21 - b11)
    p5 = strassen_multiply(a11 + a12, b22)
    p6 = strassen_multiply(a21 - a11, b11 + b12)
    p7 = strassen_multiply(a12 - a22, b21 + b22)
    # Combine the products to get the result matrix
    c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5
    c21 = p2 + p4
    c22 = p1 - p2 + p3 + p6
    # Combine the submatrices into the result matrix
    result = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return result

# Main program
if __name__ == "__main__":
    # Example matrices A and B
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    # Perform Strassen's Matrix Multiplication
    result = strassen_multiply(A, B)
    # Display the result
    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    print("\nResultant Matrix C (Strassen's Multiplication):")
    print(result)
