import timeit

from fibo_py import fibo_py
# print(fibo_py(10))
print(timeit.timeit(stmt="fibo_py(n=10000)",\
                    setup="from fibo_py import fibo_py",\
                    number=1000))

from fibo_cy import fibo_cy
# print(fibo_cy(10))
print(timeit.timeit(stmt="fibo_cy(10000)",\
                    setup="from fibo_cy import fibo_cy",\
                    number=1000))