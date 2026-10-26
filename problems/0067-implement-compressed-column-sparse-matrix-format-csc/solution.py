import torch

def compressed_col_sparse_matrix(dense_matrix: torch.Tensor):
    """
    Convert a dense matrix tensor into its Compressed Column Sparse (CSC) representation
    using PyTorch's built-in sparse CSC tensor support.

    :param dense_matrix: 2D torch.Tensor representing the dense matrix
    :return: Tuple of (values, row_indices, col_pointer) as torch.Tensors
    """
    if not isinstance(dense_matrix, torch.Tensor):
        dense_tensor = torch.tensor(dense_matrix)
    else:
        dense_tensor = dense_matrix

    dense_tensor = torch.tensor(dense_matrix)
    csc_tensor = dense_tensor.to_sparse_csc()
    
    return csc_tensor.values(), csc_tensor.row_indices(), csc_tensor.ccol_indices()