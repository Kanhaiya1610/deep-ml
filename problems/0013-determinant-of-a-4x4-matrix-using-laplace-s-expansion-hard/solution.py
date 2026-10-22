import torch

def determinant_4x4(matrix) -> float:
    """
    Compute the determinant of a 4×4 matrix using PyTorch.
    Input can be a Python list, NumPy array, or torch Tensor of shape (4,4).
    Returns a Python float.
    """
    # # Convert to tensor
    # m = torch.as_tensor(matrix, dtype=torch.float)
    # # Your implementation here
    # det = torch.linalg.det(m)
    # return m.item()

    if isinstance(matrix, torch.Tensor):
        # Ensure it is placed on CPU and uses float data type
        tensor_matrix = matrix.to(dtype=torch.float)
    elif isinstance(matrix, np.ndarray):
        tensor_matrix = torch.from_numpy(matrix).to(dtype=torch.float32)
    else:
        # Assumes input is a nested Python list
        tensor_matrix = torch.tensor(matrix, dtype=torch.float32)
        
    # 2. Compute the determinant using PyTorch's linear algebra module
    det_tensor = torch.linalg.det(tensor_matrix)
    
    # 3. Extract the scalar element out of the tensor and return it as a Python float
    return float(det_tensor.item())
    pass
