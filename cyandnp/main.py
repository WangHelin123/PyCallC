import timeit
import numpy as np

#A=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

from row_mean_py import row_mean_py

print('Python',timeit.timeit(stmt="row_mean_py(A)",\
                             setup="""
from row_mean_py import row_mean_py
import numpy as np
A=np.random.normal(size=[1000,1000])
""",\
                             number=10
))



from row_mean_cy import row_mean_cy


print('Cython',timeit.timeit(stmt="row_mean_cy(A)",\
                             setup="""
from row_mean_cy import row_mean_cy
import numpy as np
A=np.random.normal(size=[1000,1000])
""",\
                             number=10
))