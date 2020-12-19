from operator import itemgetter
from tree_format import format_tree
from asciitree import LeftAligned


class BadFormatDirectories(Exception):
    """Bad format on directories"""


class Drawer:
    """Drawer es la clase que dibuja el arbol de directorios en la consola

    Constructor
    -----------
    fmt: (str) puede ser ascii o unix. En caso de que no sean estas opciones
    se lanza NotImplementedError
    directories: es el conjunto de directorios para dibujar. Aquí se debe
    tener especial cuidado con el formato. *format_tree* recibe una tupla
    con la forma:
    tree = (
        'foo', [
            ('bar', [
                ('a', []),
                ('b', []),
            ]),
            ('baz', []),
                ('qux', [
                ('cd', []),
            ]),
        ],
    )

    y ascii_tree recibe un formato así:
    {
    'asciitree': OD([
        ('sometimes',
            {'you': {}}),
        ('just',
            {'want': OD([
                ('to', {}),
                ('draw', {}),
            ])}),
        ('trees', {}),
        ('in', {
            'your': {
                'terminal': {}
            }
        })
    ])
    }
    Donde OD viene de `from collections import OrderedDict as OD`. Eso
    es un diccionario ordenado, para no perder el "orden" de cómo se fueron
    agregandos. Se puede reemplazar el "OD([])" por "{}"

    Se podría, si se quiere hacer algo mas complejo pero, será suficiente
    por ahora check si es tuple o dict.
    """
    def __init_(self.directories, fmt: str):
        pass

    def _check_directories_and_format(self, directories):
        """Check si el directories tiene format correcto.

        Si directories es una tuple, el formato con el que se va a imprimir
        debe ser unix.
        Si directories es un dict, el formato con el que se va a imprimir
        debe ser ascii.

        Si no se cumplen ninguna de las condiciones se lanza una exception
        BadFromatDirectories
        """
        if self fmt == 'unix' and isinstance(directories, tuple):
            return directories

    def print_tree(self):
        if self.fmt = 'unix':
            format_tree(
                self.directories, format_node=itemgetter(0), get_children=itemgetter(1))
        elif self.fmt == 'ascii'
            tr = LeftAligned()
            tr(self.directories)
        else
            raise NotImplementedError

