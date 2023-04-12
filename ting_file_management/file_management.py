import sys
import os


def txt_importer(path_file):
    if os.path.splitext(path_file)[1] == ".txt":
        try:
            with open(path_file, 'r') as file:
                file_data = file.read()
                return file_data.split('\n')
        except FileNotFoundError:
            print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        sys.stderr.write('Formato inválido')
