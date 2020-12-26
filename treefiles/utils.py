def get_simulate_folder(fmt):
    """Retornar un arbol de directorios en formato de tuple necesarios
    para imprimir como tuplas, o formato dict para imprimir como ascii.
    """
    path_tree_ascii = {
    'home': {
        'eamanu': {
            'Documents': {
                'ejemplo': {
                    'ejemplo.py':{},
                    'ejemplo2.py': {}
                    },
                 'carperta_vacia': {}
                },
            'Videos': {},
            'Pictures': {}
            }
        }
    }

    path_tree_unix = (
        'home', [
            ('Documents', [
                ('ejemplo', [
                    ('ejemplo.py', []),
                    ('ejemplo2.py', [])
                ]),
                ('carperta_vacia', []),
            ]),
            ('Videos', []),
            ('Pictures', [])
            ])

    if fmt == 'unix':
        return path_tree_unix
    return path_tree_ascii
