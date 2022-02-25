import time, random
import xlsxwriter as xl
INF = 9999999
how_many = 100
how_many2 = 150
paramparampam = how_many2+1

def kraskal(d):
    pusto = []
    letters = []
    while(d):
        #print(d[0][0][0], ' -> ', d[0][0][1], ': ', d[0][1])
        if d[0][0][0] in letters and d[0][0][1] in letters:
            d = d[1:]
            continue
        pusto+=d[0]
        if d[0][0][0] not in letters:
            letters += d[0][0][0]
        if d[0][0][1] not in letters:
            letters += d[0][0][1]
        d = d[1:]
    '''for i in range(0, len(pusto), 2):
        print(pusto[i][0], ' -> ', pusto[i][1], ': ', pusto[i+1])'''

def prim(n, g):
    pusto = [0] * n
    pusto[0] = 1
    while sum(pusto) < n:
        minimum = INF
        x = 0
        y = 0
        for i in range(n):
            if pusto[i] == 1:
                for j in range(n):
                    if pusto[j] == 0 and g[i][j]:
                        if minimum > g[i][j]:
                            minimum = g[i][j]
                            x = i
                            y = j
        if g[x][y] == 0:
            print(g)
            exit(12345)
        #print(str(x) + "->" + str(y) + ": " + str(g[x][y]))
        pusto[y] = 1

def newN(n):
    return n+1#random.randint(2, paramparampam)

def newMas(n):
    #mas = [0] * (n*(n-1)//2)
    g = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i!=j:
                g[i][j] = random.randint(0, 15)
                g[j][i] = g[i][j]
        if sum((lambda g: [el for el in g])(g[i]))==0:
            return 'zero'
    return g

def sorte(d):
    d = list(d.items())
    d.sort(key=lambda i: i[1])
    return d

def sorteDelete(d):
    d = list(d.items())
    d.sort(key=lambda i: -i[1])
    return d

def vid(n, g): #new dict with edge of graph
    d = {}
    letters = tuple('ÅåÄäÀàÁáÂÇçČčÉéÈèÊêËëĔĕĞğĢģÏïÎîÍíÌìÑñÖöÔôŌōÒòÓóØøŜŝŞşÜüŪūÛûÙùÚúŸÿabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦШЩЪЫЬЭЮЯ'[:n])
    for i in range(n):
        for j in range(n):
            if g[i][j] == 0:
                continue
            if letters[i]+letters[j] not in d and letters[j]+letters[i] not in d:
                d |= {letters[i]+letters[j]:g[i][j]}
    return d


def reverseDelete(d, n):
    #pusto = []
    letters = ','.join([i[0] for i in d])
    while(len(d)>=n):
        if letters.count(d[0][0][0])<2 or letters.count(d[0][0][1])<2:
            letters = letters.replace(d[0][0], '')
            d = d[1:]+[d[0]]
            continue
        letters = letters.replace(d[0][0], '')
        d = d[1:]
    #d.sort()            #для красоты
    #for i in d:
        #print(i[0][0], ' -> ', i[0][1], ': ', i[1])


n=1
middle1 = [[0 for i in range(paramparampam+1)]for j in range(2)]
middle2 = [[0 for i in range(paramparampam+1)]for j in range(3)]
middle3 = [[0 for i in range(paramparampam+1)]for j in range(3)]
'''file = open('prim.txt', 'w')'''
for i in range(how_many2):
    n = newN(n)
    for j in range(how_many):
        g = 'zero'
        while g == 'zero':
            g = newMas(n)
        start_time = time.perf_counter()  # начинаем время
        # time.sleep(0.1)
        prim(n, g)
        middle1[0][n] += (time.perf_counter() - start_time)
        middle1[1][n] += 1
        '''file.write(str(n))
        file.write(' ' + str(time.time() - start_time-0.1) + '\n')'''
        print("%s секунд" % (time.perf_counter() - start_time))

        g = vid(n, g)
        start_time = time.perf_counter()  # начинаем время
        # time.sleep(0.1)
        gD = sorteDelete(g)
        middle2[0][n] += (time.perf_counter() - start_time)
        start_time = time.perf_counter()  # начинаем время
        # time.sleep(0.1)
        reverseDelete(gD, n)
        middle2[1][n] += (time.perf_counter() - start_time)
        middle2[2][n] += 1
        print("%s секунд" % (time.perf_counter() - start_time))

        start_time = time.perf_counter()  # начинаем время
        # time.sleep(0.1)
        g = sorte(g)
        middle3[0][n] += (time.perf_counter() - start_time)
        start_time = time.perf_counter()  # начинаем время
        # time.sleep(0.1)
        kraskal(g)
        middle3[1][n] += (time.perf_counter() - start_time)
        middle3[2][n] += 1
        print("%s секунд" % (time.perf_counter() - start_time))

'''file.close()'''
workbook = xl.Workbook('prim.xlsx')
worksheet = workbook.add_worksheet()
for i in range(2, paramparampam+1):
    worksheet.write(i-2, 0, i)
    worksheet.write(i-2, 1, middle1[0][i]/(middle1[1][i] if middle1[1][i]!=0 else 1))
workbook.close()

workbook = xl.Workbook('reverseDelete.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, 'матрица')
worksheet.write(0, 1, 'время сортировки')
worksheet.write(0, 2, 'обр удаление')
for i in range(2, paramparampam+1):
    worksheet.write(i-1, 0, i)
    worksheet.write(i-1, 1, middle2[0][i]/(middle2[2][i] if middle2[2][i]!=0 else 1))
    worksheet.write(i-1, 2, middle2[1][i]/(middle2[2][i] if middle2[2][i] != 0 else 1))
workbook.close()

workbook = xl.Workbook('kraskal.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, 'матрица')
worksheet.write(0, 1, 'время сортировки')
worksheet.write(0, 2, 'краскал')
for i in range(2, paramparampam+1):
    worksheet.write(i-1, 0, i)
    worksheet.write(i-1, 1, middle3[0][i]/(middle3[2][i] if middle3[2][i]!=0 else 1))
    worksheet.write(i-1, 2, middle3[1][i]/(middle3[2][i] if middle3[2][i] != 0 else 1))
workbook.close()