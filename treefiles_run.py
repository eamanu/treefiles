import argparse

from treefiles.tree import Tree


def run(path, fmt):
    t = Tree()
    t(path, fmt)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pretty tree files')
    parser.add_argument('folder', metavar='P', type=str,
                    help='Path to the folder to show the tree directory')
    parser.add_argument('--format', '-f', default='unix',
                        help='format of the tree (default: unix)')

    args = parser.parse_args()
    if args.folder:
        run(args.folder, args.format)
