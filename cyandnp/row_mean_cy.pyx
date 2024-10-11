import numpy as np
import cython

@cython.wraparound(False)
@cython.boundscheck(False)
@cython.cdivision(True)
def row_mean_cy(A):
    A=A.astype(np.intc)
    out = np.zeros(A.shape[0],dtype=np.double)
    
    # cautious np.array.detype which as cdef
    # which need to def double or A.astype(np.intc)
    
    cdef double[:] out_view = out
    cdef int[:,:] A_view = A

    cdef Py_ssize_t i 
    cdef Py_ssize_t j
    cdef int m = A.shape[0]
    cdef int n = A.shape[1]

    for i in range(m):
        for j in range(n):
            out_view[i] += <double> A_view[i,j]/n
    return out