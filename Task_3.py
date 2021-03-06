def thesaurus(*names):
    first_letters = []
    for name in names:
        first_letters.append(name[0])
    result_dict = {}
    for key in first_letters:
        result_dict[key] = list()
    for name in names:
        result_dict[name[0]].append(name)
    result_dict_sort = {}
    for key in sorted(result_dict):
        result_dict_sort[key] = result_dict[key]
    return print(result_dict_sort)


thesaurus("Ярослав", "Иван", "Петр", "Мария", "Игорь", "Максим")
