import cython

@cython.wraparound(False)
@cython.boundscheck(False)
def fibo_cy(int n):
    cdef int a1=1
    cdef int a2=1
    cdef int out=0
    cdef int i
    for i in range(n-2):
        out=a1+a2
        a1=a2
        a2=out
    return out

