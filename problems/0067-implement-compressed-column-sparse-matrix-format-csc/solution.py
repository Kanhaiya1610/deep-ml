import numpy as np

def compressed_col_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	num_rows = len(dense_matrix)
	num_cols = len(dense_matrix[0]) if num_rows > 0 else 0
	values = []
	row_indices = []
	col_ptr = [0]

	running_nonzero_count = 0

	for j in range(num_cols):
		for i in range(num_rows):
			val = dense_matrix[i][j]

			if val != 0:
				values.append(val)
				row_indices.append(i)
				running_nonzero_count+=1

		col_ptr.append(running_nonzero_count)

	return values, row_indices, col_ptr
