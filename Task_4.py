import os
from collections import defaultdict

folder = './some_data'
file_stat = []
dir_stat_tmp = defaultdict(list)
for root, dirs, files in os.walk(folder):
    for file in files:
        f_path = os.path.join(root, file)
        file_stat.append(os.stat(f_path).st_size)
for el in file_stat:
    if el <= 10 ** 2:
        dir_stat_tmp[10 ** 2].append(el)
    elif 10 ** 2 < el <= 10 ** 3:
        dir_stat_tmp[10 ** 3].append(el)
    elif 10 ** 3 < el <= 10 ** 4:
        dir_stat_tmp[10 ** 4].append(el)
    elif 10 ** 4 < el <= 10 ** 5:
        dir_stat_tmp[10 ** 5].append(el)
dir_stat = {}
for key in sorted(dir_stat_tmp):
    dir_stat[key] = len(dir_stat_tmp[key])

print(f'Всего файлов в папке "{folder}": {len(file_stat)} шт.\n{dir_stat}')
