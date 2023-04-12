import sys
import os


def txt_importer(path_file):
    if os.path.splitext(path_file)[1] == ".txt":
        try:
            with open(path_file, 'r') as file:
                file_data = file.read()
                return file_data.split('')
        except FileNotFoundError:
            return f"Arquivo {path_file} não encontrado", file
    else:
        sys.stderr.write('Formato inválido')
