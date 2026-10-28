import numpy as np

def rref(matrix):
	A = np.array(matrix, dtype=np.float64)
	num_rows, num_cols = A.shape
	pivot_row = 0
	tolerance = 1e-9
	for col in range(num_cols):
		if pivot_row >= num_rows:
			break
		max_row = pivot_row + np.argmax(np.abs(A[pivot_row:, col]))
		if np.abs(A[max_row, col]) < tolerance:
			continue
		if max_row != pivot_row:
			A[[pivot_row, max_row]] = A[[max_row, pivot_row]]
		pivot_val = A[pivot_row, col]
		A[pivot_row] = A[pivot_row] / pivot_val
		for r in range(num_rows):
			if r != pivot_row:
				factor = A[r, col]
				A[r] = A[r] - factor * A[pivot_row]
		pivot_row += 1
	A[np.abs(A) < tolerance] = 0.0
	return A.tolist()
