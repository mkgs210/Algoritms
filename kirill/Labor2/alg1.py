# Алгоритм Бойера — Мура


def forming_d(pattern):
    """ Формируем массив d."""
    d = [len(pattern) for i in range(256)]
    new_p = pattern[::-1]

    for i in range(len(new_p)):
        if d[ord(new_p[i])] != len(new_p):
            continue
        else:
            d[ord(new_p[i])] = i
    return d


def search(string, pattern):
    """ Поиск Бойера - Мура."""

    d = forming_d(pattern)
    # x - начало прохода по string
    # j - проход по pattern
    # k - проход по string
    len_p = x = j = k = len(pattern)
    # число смещений
    counter = 0

    while x <= len(string) and j > 0:
        if pattern[j - 1] == string[k - 1]:
            j -= 1
            k -= 1
        else:
            x += d[ord(string[k - 1])]
            k = x
            j = len_p
            counter += 1

    if j <= 0:
        return "Подстрока начинается с %d индекса" % k
    else:
        return "Не нашли!"


string = "dsjhjhjpfefbubajsnf"
pattern = "buba"
print()
print(search(string, pattern))
