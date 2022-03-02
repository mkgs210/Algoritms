import time
import random
import xlsxwriter as xl

# Прямой пребор (в лоб)

def stringSearch(s, x):
    i=j=0
    lengthS = len(s)# Длина строки в которой ищем
    lengthX = len(x)# -||- которую ищем
    # пока не достигли одного из концов
    while i<=lengthS - lengthX and j<lengthX:
     # если совпали буквы продвигаемся по обеим строкам
        if s[i+j]==x[j]:
            j+=1
        # иначе двигаемся по строке(+1), начиная с 0 символа подстроки
        else:
            i+=1
            j=0
    # если дошли до конца подстроки - нашли, иначе - нет
    return i if j==lengthX else -1


x = [i for i in range(10, 20011,100)]
y = []

alph = "abcdef"
for i in x:

    pattern = "dadae"
    sek=0
    for j in range(1000):
        #rand_string = ''.join(random.choice(alph) for j in range(i - 5))
        #gen_chisl = random.randint(i//2-1, i - 5)
        gen_chisl=i-5
        #rand_string = rand_string[:gen_chisl] + pattern + rand_string[gen_chisl:]
        rand_string = ("abcde" * (i // 2))[:gen_chisl] + pattern
        # rand_pattern = ''.join(random.choice(alph) for j in range(5))

        #print(rand_string)
        #print(len(rand_string))
        start_time = time.perf_counter()
        #print(1)
        prov = stringSearch(rand_string,pattern)
        #prov = search("dbaeedadae", pattern)
        #print(1)
        sek += time.perf_counter() - start_time

    sek /= 1000
    print(rand_string)

    print(prov)
    if prov!=-1:
        print(f"Подстрока начинается с {prov} индекса")
    else:
        print(prov)
    print(sek, "seconds")
    y.append(sek)
    #print(len(y))
    print()

workbook = xl.Workbook('vlob.xlsx')
worksheet = workbook.add_worksheet()
for i in range(0, len(x)):
    worksheet.write(i+2, 0, x[i])
    worksheet.write(i+2, 1, y[i])
workbook.close()

