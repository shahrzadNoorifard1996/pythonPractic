from distutils.core import setup,Extension
from Cython.Build import cythonize

ext=Extension(name="pnom",sources=["pnom.pyx"])
setup(ext_modules=cythonize(ext))