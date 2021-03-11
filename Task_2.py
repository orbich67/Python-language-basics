first_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
second_list = []
for text in first_list:
    if text.isdigit():
        second_list.append('"')
        if len(text) == 1:
            text = '0' + text
        second_list.append(text)
        second_list.append('"')
    elif len(text) > 1 and text[1].isdigit():
        second_list.append('"')
        text = text[0] + '0' + text[1]
        second_list.append(text)
        second_list.append('"')
    else:
        second_list.append(text)
print(second_list)

second_list = ' '.join(second_list)
print('Первый вариант вывода: ', second_list)

second_list = (second_list[0:3] + second_list[4:6]
               + second_list[7:16] + second_list[17:19]
               + second_list[20:54] + second_list[55:58]
               + second_list[59:69])
print('Второй вариант вывода: ',second_list)
