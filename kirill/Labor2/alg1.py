import time
import random
import xlsxwriter as xl


# Алгоритм Бойера-Мура-Хорспула


def forming_d(t):
    S = set()  # уникальные символы в образе
    M = len(t)  # число символов в образе
    d = {}  # словарь смещений

    for i in range(M - 2, -1, -1):  # итерации с предпоследнего символа
        if t[i] not in S:  # если символ еще не добавлен в таблицу
            d[t[i]] = M - i - 1
            S.add(t[i])

    if t[M - 1] not in S:  # отдельно формируем последний символ
        d[t[M - 1]] = M

    d['*'] = M  # смещения для прочих символов

    return d


def search(string, t):
    a = string
    N = len(a)
    M = len(t)
    d = forming_d(t)
    if N >= M:
        i = M - 1  # счетчик проверяемого символа в строке

        while (i < N):
            k = 0
            j = 0
            flBreak = False
            for j in range(M - 1, -1, -1):
                if a[i - k] != t[j]:
                    if j == M - 1:
                        off = d[a[i]] if d.get(a[i], False) else d[
                            '*']  # смещение, если не равен последний символ образа
                    else:
                        off = d[t[j]]  # смещение, если не равен не последний символ образа

                    i += off  # смещение счетчика строки
                    flBreak = True  # если несовпадение символа, то flBreak = True
                    break

                k += 1  # смещение для сравниваемого символа в строке

            if not flBreak:  # если дошли до начала образа, значит, все его символы совпали
                return i - k + 1
        else:
            return -1
    else:
        return -1


x = [i for i in range(10, 5011, 100)]
y = []

alph = "abcdef"
for i in x:
    pattern = "dadae"
    sek=0
    for j in range(10000):
        # rand_string = ''.join(random.choice(alph) for j in range(i - 5))
        # gen_chisl = random.randint(i//2-1, i - 5)
        gen_chisl = i - 5
        # rand_string = rand_string[:gen_chisl] + pattern + rand_string[gen_chisl:]
        rand_string = ("abcde" * (i // 2))[:gen_chisl] + pattern
        # rand_pattern = ''.join(random.choice(alph) for j in range(5))

        # print(rand_string)
        # print(len(rand_string))
        start_time = time.perf_counter()
        # print(1)
        prov = search(rand_string, pattern)
        # prov = search("dbaeedadae", pattern)
        # print(1)
        sek += time.perf_counter() - start_time

    sek/=1000
    print(rand_string)


    print(f"образ найден по индексу {prov}")
    print(sek, "seconds")
    y.append(sek)
    # print(len(y))
    print()

workbook = xl.Workbook('boer_mur_horsp.xlsx')
worksheet = workbook.add_worksheet()
for i in range(0, len(x)):
    worksheet.write(i + 2, 0, x[i])
    worksheet.write(i + 2, 1, y[i])
workbook.close()
