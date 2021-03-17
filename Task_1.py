with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    parsing_log = []
    line_log = 0
    for line in file:
        remote_adr = str(line.split(' - -')[:-1])
        remote_adr = remote_adr[2:-2]
        request_type = line.split('] "')
        request_type = request_type[1].split(' /')[0]
        requested_resource = line.split('/d')
        requested_resource = '/d' + requested_resource[1].split(' HTTP')[0]
        parsing_data = (remote_adr, request_type, requested_resource)
        parsing_log.append(parsing_data)
        line_log += 1
print('Количество строк в файле nginx_logs.txt: ', line_log)
print('Количество кортежей в списке parsing_log: ', len(parsing_log))
print('Пример кортежей из списка parsing_log: ', parsing_log[217:218], parsing_log[9999:10000])
