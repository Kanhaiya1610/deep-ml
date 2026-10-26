import numpy as np

def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	v_np = np.array(v, dtype=np.float64)
	L_np = np.array(L, dtype=np.float64)

	numerator = np.dot(v_np, L_np)
	denominator = np.dot(L_np, L_np)

	if denominator == 0:
		return -1

	projection = (numerator / denominator) * L_np

	return np.round(projection, decimals=1).tolist()