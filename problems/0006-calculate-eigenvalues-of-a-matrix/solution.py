import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a = np.array(matrix)

	try:
		eigenvalues = sorted(np.linalg.eigvals(a).tolist(),key=abs,reverse=True)
		return eigenvalues
	except np.linalg.LinAlgError:
		return []