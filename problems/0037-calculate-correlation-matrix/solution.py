import numpy as np

def calculate_correlation_matrix(X, Y=None):
	# Your code here
	Mean_X= np.mean(X, axis=0)

	centered_X = X - Mean_X

	std_X = np.std(X, axis=0, ddof=1)

	if Y is not None:

	    Mean_Y = np.mean(Y, axis=0)

	    centered_Y = Y - Mean_Y

	    std_Y = np.std(Y, axis=0, ddof=1)

	    cov_matrix = np.dot(centered_X.T, centered_Y) / (X.shape[0] - 1)

	    corr_matrix = cov_matrix / np.outer(std_X, std_Y)

	    return corr_matrix

	else:

	    cov_matrix = np.dot(centered_X.T, centered_X) / (X.shape[0] - 1)

	    corr_matrix = cov_matrix / np.outer(std_X, std_X)

	    return corr_matrix