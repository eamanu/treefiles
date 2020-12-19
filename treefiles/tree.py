import pathlib

from treefiles.utils import get_simulate_folder
from treefiles.drawer import Drawer

class Tre:
    def __init__(self):
        """No hacer nada aca, todo en __call__"""
        self.fmt = ''

    def __call___(self.path, fmt):
        """este metodo hace que se imprima el path en un formato determinado

        Se debe capturar los errores que puedan ocurrir e imprimir
        un mensaje de error.
        """
        self.fmt = fmt

    def get_directories_structure(self, path):
        # implement this
        return get_simulate_folder(self.fmt)
