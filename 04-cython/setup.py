from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize([r"C:\Users\Rodrigo\Documents\Documentos_do_Rodrigo\cursos\Assincrono_e_concorrente\04-cython\cumprimenta.pyx"])
)