from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("fibo_cy.pyx",annotate=True)
)
  