import numpy as np

def complete_pivot(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(A)

    # To keep track of column swaps
    col_index = np.arange(n)

    for k in range(n - 1):

        # Find pivot (max element) in the submatrix A[k:, k:]
        i, j = np.unravel_index(np.argmax(abs(A[k:, k:])), (n - k, n - k))
        i += k
        j += k

        # Swap rows
        if i != k:
            A[[k, i]] = A[[i, k]]
            b[[k, i]] = b[[i, k]]

        # Swap columns
        if j != k:
            A[:, [k, j]] = A[:, [j, k]]
            col_index[[k, j]] = col_index[[j, k]]

        # Elimination
        for r in range(k + 1, n):
            factor = A[r, k] / A[k, k]
            A[r, k:] -= factor * A[k, k:]
            b[r] -= factor * b[k]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(a[i, i+1:], x[i+1:]) / A[i, i]

    # Reorder solution according to swapped columns
    final_x = np.zeros(n)
    final_x[col_index] = x

    return final_x


# Example
A = np.array([[6, 2, 3],
              [1, 3, 4],
              [2, 1, 3]])

b = np.array([5, 14, 13])

print(complete_pivot(A, b))
