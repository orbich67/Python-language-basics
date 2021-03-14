tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def tut_klas_gen(tut, klas):
    if len(tut) > len(klas):
        klas_idx = len(tut) - len(klas)
        for idx in range(klas_idx):
            klas.append(None)
    for idx in range(len(tut)):
        if idx <= len(tut):
            yield tut[idx], klas[idx]


print(type(tut_klas_gen(tutors, klasses)))
tut_klas = tut_klas_gen(tutors, klasses)
for value in tut_klas:
    print(value)
