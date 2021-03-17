def user_hobby(users_file, hobby_file):
    with open(users_file, 'r', encoding='utf-8') as file_1, open(hobby_file, 'r', encoding='utf-8') as file_2:
        users = []
        for line in file_1:
            users.append(line.replace('\n', ''))
        hobby = []
        for line in file_2:
            hobby.append(line.replace('\n', ''))
    with open('users_hobby.txt', 'a', encoding='utf-8') as file_3:
        for idx in range(len(users)):
            if len(users) > len(hobby):
                hobby_idx = len(users) - len(hobby)
                for num in range(hobby_idx):
                    hobby.append(None)
            elif len(users) == len(hobby):
                pass
            else:
                with open('users_hobby.txt', 'w', encoding='utf-8') as f:
                    f.write(f'Process finished with exit code 1')
                exit(1)
            file_3.write(f'{users[idx]}: {hobby[idx]}\n')


user_hobby('users.csv', 'hobby.csv')
