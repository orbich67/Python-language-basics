import re

RE_LOG_PARSER = re.compile(r'([a-z0-9.:]+)\s-\s-\s\[([A-za-z/:\s+0-9]+)]\s\"([A-Z]+)\s'
                           r'([_/0-9a-z]+)\s[A-Z/.0-9]+\"\s([0-9]+)\s([0-9]+)\s')

with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    parsing_log = []
    line_log = 0
    for line in file:
        parsing_log.append(RE_LOG_PARSER.findall(line))
        line_log += 1

print('Количество строк в файле nginx_logs.txt: ', line_log)
print('Количество элементов в списке parsing_log: ', len(parsing_log))
print('Пример записи в parsing_log:', parsing_log[217], parsing_log[3895], parsing_log[9999])
