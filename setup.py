import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("BuscaGulosa.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = ["mapa.png"],
        excludes = []
)

setup(
    name = "BuscaGulosa",
    version = "1.0",
    description = "Programa que busca uma rota entre os os maiores aeroportos da America Latina",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
