import pathlib

from treefiles.utils import get_simulate_folder
from treefiles.drawer import Drawer

class Tree:
    def __init__(self):
        self.fmt = ''

    def __call__(self, path, fmt):
        """este metodo hace que se imprima el path en un formato determinado

        Se debe capturar los errores que puedan ocurrir e imprimir
        un mensaje de error.
        """
        self.fmt = fmt
        d = Drawer(self.get_directories_structure(path), fmt)
        d.print_tree()

    def get_directories_structure(self, path):
        # implement this
        return get_simulate_folder(self.fmt)
