from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("row_mean_cy.pyx",annotate=True)
)
  