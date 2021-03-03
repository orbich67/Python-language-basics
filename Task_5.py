from random import choice


def get_jokes(numbers, repeat=True):
    """
    Prints string of three random words taken from three random lists (one from each)

    :param numbers: number of rows returned
    :param repeat: True  - repeat words in a line, False - no repeat words in a line.
    """
    nouns_tmp = nouns[:]
    adverbs_tmp = adverbs[:]
    adjectives_tmp = adjectives[:]
    nouns_new = []
    adverbs_new = []
    adjectives_new = []
    jokes = []
    if repeat:
        for number in range(numbers):
            jokes.extend([f'{choice(nouns_tmp)} {choice(adverbs_tmp)} {choice(adjectives_tmp)}'])
        print(jokes)
        return
    for number in range(numbers):
        nouns_new.append(choice(nouns_tmp))
        nouns_tmp.remove(nouns_new[number])
        adverbs_new.append(choice(adverbs_tmp))
        adverbs_tmp.remove(adverbs_new[number])
        adjectives_new.append(choice(adjectives_tmp))
        adjectives_tmp.remove(adjectives_new[number])
        jokes.extend([f'{nouns_new[number]} {adverbs_new[number]} {adjectives_new[number]}'])
    print(jokes)


nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']
get_jokes(3)
get_jokes(3, False)
