from distutils.core import setup
from Cython.Build import cythonize
# setup(
#     ext_modules = cythonize("cy_primes.pyx")
#     )

setup(
    ext_modules = cythonize("fastloop.pyx")
    )