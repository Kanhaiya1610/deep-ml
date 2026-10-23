from tinygrad.tensor import Tensor
import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]):
    """
    Transforms matrix A using T^{-1} A S.
    Validates that T and S are invertible. Returns -1 if not.
    Uses Tinygrad's matmul for the transformation.
    """
    try:
        T_inv_np = np.linalg.inv(np.array(T))
        S_inv_np = np.linalg.inv(np.array(S))
    except (np.linalg.LinAlgError, ValueError):
        return -1
    
    A_tensor = Tensor(A, dtype=None)
    S_tensor = Tensor(S, dtype=None)
    T_inv_np = Tensor(T_inv_np.tolist(), dtype=None)

    t_tensor = T_inv_np @ A_tensor @ S_tensor 

    return t_tensor.numpy().tolist()