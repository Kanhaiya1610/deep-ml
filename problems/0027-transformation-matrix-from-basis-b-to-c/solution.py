import numpy as np

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	b = np.array(B)
	c_inv = np.linalg.inv(np.array(C))
	P = np.matmul(c_inv, b)

	return np.round(P, decimals=4).tolist()