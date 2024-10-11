import numpy as np

def row_mean_py(A):
    out = np.zeros(A.shape[0])
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            out[i] += A[i,j]/A.shape[1]
    return out


