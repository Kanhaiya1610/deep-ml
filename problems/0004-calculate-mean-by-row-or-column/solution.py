import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == 'column':
		col = np.mean(matrix, axis=0)
		means = col.tolist()
	else:
		row = np.mean(matrix, axis = 1)
		means = row.tolist()
	return means