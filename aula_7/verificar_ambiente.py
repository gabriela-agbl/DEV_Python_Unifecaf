# Diagnóstico de ambiente; não corrige nem instala programas.
import sys
from importlib.metadata import version, PackageNotFoundError
print("Python:", sys.version.split()[0])
print("Executável:", sys.executable)
try:
    print("pytest:", version("pytest"))
except PackageNotFoundError:
    print("pytest: ausente; siga COMECE_AQUI.md para instalar.")
print("unittest: faz parte da biblioteca padrão do Python.")
