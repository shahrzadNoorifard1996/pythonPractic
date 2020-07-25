from distutils.core import setup,Extension
from Cython.Build import cythonize

ext=Extension(name="pnmt",sources=["pnmt.pyx"])
setup(ext_modules=cythonize(ext))