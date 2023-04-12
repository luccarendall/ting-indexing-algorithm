from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for position in range(len(instance)):
        if path_file in instance.search(position).values():
            return None

    file_data = txt_importer(path_file)
    lines = len(file_data)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": lines,
        "linhas_do_arquivo": file_data
    }

    instance.enqueue(result)
    print(result, file=sys.stdout)
    # https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
