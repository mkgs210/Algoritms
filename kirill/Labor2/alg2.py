import time
import random
import xlsxwriter as xl


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


x = [i for i in range(10, 50011,100)]
y = []

alph = "abcdef"
for i in x:

    pattern = "dadae"
    sek=0
    for j in range(100):
        #rand_string = ''.join(random.choice(alph) for j in range(i - 5))
        #gen_chisl = random.randint(i//2-1, i - 5)
        gen_chisl = i - 5
        #rand_string = rand_string[:gen_chisl] + pattern + rand_string[gen_chisl:]
        rand_string = ("abcde"*(i//2))[:gen_chisl]+pattern
        # rand_pattern = ''.join(random.choice(alph) for j in range(5))

        # print(rand_string)
        # print(len(rand_string))
        start_time = time.perf_counter()
        # print(1)
        prov = kmp(pattern, rand_string)
        # prov = search("dbaeedadae", pattern)
        # print(1)
        sek += time.perf_counter() - start_time

    sek /= 100
    print(rand_string)

    print(prov)
    if prov != -1:
        print(f"Подстрока начинается с {prov} индекса")
    else:
        print(prov)
    print(sek, "seconds")
    y.append(sek)
    # print(len(y))
    print()

workbook = xl.Workbook('knut_morr_prat.xlsx')
worksheet = workbook.add_worksheet()
for i in range(0, len(x)):
    worksheet.write(i + 2, 0, x[i])
    worksheet.write(i + 2, 1, y[i])
workbook.close()
