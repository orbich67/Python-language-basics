first_list = ['инженер-конструктор Игорь','главный бухгалтер МАРИНА','токарь высшего разряда нИКОЛАй','директор аэлита']
for text in first_list:
    idx = 0
    text = text[::-1]
    name = ''
    while True:
        if text[idx] != ' ':
            name += text[idx]
            idx += 1
        else:
            name = name[::-1]
            name = name.title()
            print(f'Привет, {name}!')
            break
