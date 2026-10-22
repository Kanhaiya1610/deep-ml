import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    m = np.array(matrix)
    
    if m.ndim != 2 or m.shape[0] != m.shape[1]:
        return None
        
    try:
        inverse_m = np.linalg.inv(m)
        return inverse_m.tolist()
    except np.linalg.LinAlgError:
        return None
    pass