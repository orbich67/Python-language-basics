# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
# a) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#    Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
#    Внимание: использовать только арифметические операции!
# b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
#    сумма цифр которых делится нацело на 7.
# c) * Решить задачу под пунктом b, не создавая новый список.

# создаем список из кубов нечетных чисел от 1 до 1000
numbers = []
for number in range(1, 1000 + 1):
    if number %2 != 0:
        numbers.append(number ** 3)

# список кубов чисел от 1 до 1000 сумма чисел которых кратна 7
numbers_multiple = []
for number in numbers:
    multiple_number = number
    sum_number = 0
    while number > 0:
        sum_number = sum_number + number % 10
        number = number // 10
    if sum_number %7 == 0:
        numbers_multiple.append(multiple_number)

# вычисляем сумму чисел списка numbers_multiple
sum_number = 0
for number in numbers_multiple:
    sum_number += number

print('a) Сумма чисел из списка: ', sum_number)

# к каждому элементу первого списка добавляем 17
for number in range(len(numbers)):
    numbers[number] = numbers[number] + 17

# список из чисел списка numbers, сумма цифр которых кратна 7
numbers_multiple = []
for number in numbers:
    multiple_number = number
    sum_number = 0
    while number > 0:
        sum_number = sum_number + number % 10
        number = number // 10
    if sum_number %7 == 0:
        numbers_multiple.append(multiple_number)

# вычисляем сумму чисел списка numbers_multiple
sum_number = 0
for number in numbers_multiple:
    sum_number += number

print('b) Сумма чисел из списка: ', sum_number)
