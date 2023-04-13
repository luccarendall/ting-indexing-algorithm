def exists_word(word, instance):
    search_result = []
    for file in range(0, len(instance)):
        occurrences = []
        # itera sobre cada elemento da lista "linhas_do_arquivo" retornada
        # pelo método search() e atribui a cada elemento uma variável
        # "actual_line" e um índice.
        for index, actual_line in enumerate(
                instance.search(file)['linhas_do_arquivo']
                ):
            # verifica se a palavra em word está presente na linha atual
            if word.lower() in actual_line.lower():
                occurrences.append({"linha": index + 1})

        result = {
            "palavra": word,
            "arquivo": instance.search(file)['nome_do_arquivo'],
            "ocorrencias": occurrences
        }
        if occurrences:
            search_result.append(result)

    return search_result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
