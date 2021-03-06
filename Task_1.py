# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:

# a) до минуты: <s> сек;
intervals = [1, 11, 59]
for duration in intervals:
    seconds = duration % 60
    print(seconds, 'сек')

# b) до часа: <m> мин <s> сек;
intervals = [61, 671, 3599]
for duration in intervals:
    duration = duration % (60 * 60)
    minutes = duration // 60
    seconds = duration % 60
    print(minutes, 'мин', seconds, 'сек')

# c) до суток: <h> час <m> мин <s> сек;
intervals = [3661, 40271, 86399]
for duration in intervals:
    duration = duration % (60 * 60 * 24)
    hours = duration // (60 * 60)
    duration = duration % (60 * 60)
    minutes = duration // 60
    seconds = duration % 60
    print(hours, 'час', minutes, 'мин', seconds, 'сек')

# d) * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
intervals = [90061, 990671, 2678399]
for duration in intervals:
    duration = duration % (60 * 60 * 24 * 31)
    days = duration // (60 * 60 * 24)
    duration = duration % (60 * 60 * 24)
    hours = duration // (60 * 60)
    duration = duration % (60 * 60)
    minutes = duration // 60
    seconds = duration % 60
    print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
