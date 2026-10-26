import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	values = []
	column_indices = []
	row_pointer = [0]

	running_nonzero_count = 0

	for row in dense_matrix:
		for j, val in enumerate(row):
			if val!= 0:
				values.append(val)
				column_indices.append(j)
				running_nonzero_count+=1
		
		row_pointer.append(running_nonzero_count)
	
	return values, column_indices, row_pointer