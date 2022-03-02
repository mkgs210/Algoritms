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


# Алгоритм Кнута — Морриса — Пратта

def prefix(s):
    P = [0] * len(s)
    j = 0
    i = 1

    while i < len(s):
        if s[j] != s[i]:
            if j > 0:
                j = P[j - 1]
            else:  # j == 0
                i += 1
        else:  # s[j] == s[i]
            P[i] = j + 1
            i += 1
            j += 1

    return P


def kmp(sub: str, s: str):
    k = 0
    l = 0
    P = prefix(sub)

    while k < len(s):
        if sub[l] == s[k]:
            k += 1
            l += 1

            if l == len(sub):
                return k - len(sub)

        elif l > 0:
            l = P[l - 1]
        else:
            k += 1

    return -1


# Прямой пребор (в лоб)

def stringSearch(s, x):
    i = j = 0
    lengthS = len(s)  # Длина строки в которой ищем
    lengthX = len(x)  # -||- которую ищем
    # пока не достигли одного из концов
    while i <= lengthS - lengthX and j < lengthX:
        # если совпали буквы продвигаемся по обеим строкам
        if s[i + j] == x[j]:
            j += 1
        # иначе двигаемся по строке(+1), начиная с 0 символа подстроки
        else:
            i += 1
            j = 0
    # если дошли до конца подстроки - нашли, иначе - нет
    return i if j == lengthX else -1


x1 = [i for i in range(10, 2011, 50)]
x2 = [i for i in range(10, 2011, 50)]
x3 = [i for i in range(10, 2011, 50)]
y1 = []
y2 = []
y3 = []

alph = "abcdef"
for i in x1:
    pattern = "dadae"
    sek1 = 0
    sek2 = 0
    sek3 = 0
    for j in range(10000):
        # Подстрока в случайном месте
        rand_string = ''.join(random.choice(alph) for j in range(i - 5))
        gen_chisl = random.randint(0, i - 5)
        rand_string = rand_string[:gen_chisl] + pattern + rand_string[gen_chisl:]

        # Подстрока всегда в конце
        # gen_chisl = i - 5
        # rand_string = ("abcde" * (i // 2))[:gen_chisl] + pattern

        # rand_pattern = ''.join(random.choice(alph) for j in range(5))

        # 1
        start_time = time.perf_counter()
        prov1 = search(rand_string, pattern)
        sek1 += time.perf_counter() - start_time

        # 2
        start_time = time.perf_counter()
        prov2 = kmp(pattern, rand_string)
        sek2 += time.perf_counter() - start_time

        # 3
        start_time = time.perf_counter()
        prov3 = stringSearch(rand_string, pattern)
        sek3 += time.perf_counter() - start_time

    sek1 /= 1000
    sek2 /= 1000
    sek3 /= 1000

    # print(rand_string)
    print(i)
    print(f"Алгоритм Бойера-Мура-Хорспула - {sek1}\n"
          f"Алгоритм Кнута — Морриса — Пратта - {sek2}\n"
          f"Прямой пребор (в лоб) - {sek3}\n")
    y1.append(sek1)
    y2.append(sek2)
    y3.append(sek3)
    print()

workbook1 = xl.Workbook('boer_mur_horsp.xlsx')
workbook2 = xl.Workbook('knut_morr_prat.xlsx')
workbook3 = xl.Workbook('vlob.xlsx')

worksheet1 = workbook1.add_worksheet()
worksheet2 = workbook2.add_worksheet()
worksheet3 = workbook3.add_worksheet()

for i in range(0, len(x1)):
    worksheet1.write(i + 2, 0, x1[i])
    worksheet1.write(i + 2, 1, y1[i])

    worksheet2.write(i + 2, 0, x2[i])
    worksheet2.write(i + 2, 1, y2[i])

    worksheet3.write(i + 2, 0, x3[i])
    worksheet3.write(i + 2, 1, y3[i])

workbook1.close()
workbook2.close()
workbook3.close()
