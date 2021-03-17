import json


def user_hobby(users_file, hobby_file):
    with open(users_file, 'r', encoding='utf-8') as file_1, open(hobby_file, 'r', encoding='utf-8') as file_2:
        content = file_1.read()
        users = list(content.split('\n'))
        content = file_2.read()
        hobby = list(content.split('\n'))
    users_hobby = {}
    for idx in range(len(users)):
        if len(users) > len(hobby):
            hobby_idx = len(users) - len(hobby)
            for num in range(hobby_idx):
                hobby.append(None)
        elif len(users) == len(hobby):
            pass
        else:
            with open('users_hobby.csv', 'w', encoding='utf-8') as file_3:
                file_3.write(f'Process finished with exit code 1')
            exit(1)
        users_hobby[users[idx]] = hobby[idx]

    with open('users_hobby.csv', 'w', encoding='utf-8') as file_1:
        json.dump(users_hobby, file_1)


user_hobby('users.csv', 'hobby.csv')
with open('users_hobby.csv', 'r', encoding='utf-8') as f:
    print(json.load(f))
