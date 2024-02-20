from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules=cythonize('D:/十九/Desktop/云销通小组件/源码/Project1/PYD/API.py',language_level = '3'))