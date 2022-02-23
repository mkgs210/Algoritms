import time, random
import xlsxwriter as xl
how_many = 5000
paramparampam = 100

def sorte(d):
    d = list(d.items())
    d.sort(key=lambda i: -i[1])
    return d

def vid(n, g): #new dict with edge of graph
    d = {}
    letters = [*'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦШЩЪЫЬЭЮЯ'[:n]]
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

def newN():
    return random.randint(2, paramparampam)

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

middle = [[0 for i in range(paramparampam+1)]for j in range(3)]
for i in range(how_many):
    g = 'zero'
    n = newN()
    while g == 'zero':
        g = newMas(n)
    g = vid(n, g)
    start_time = time.time() #начинаем время
    time.sleep(0.1)
    g = sorte(g)
    middle[0][n] += (time.time() - start_time-0.1)
    start_time = time.time()  # начинаем время
    time.sleep(0.1)
    reverseDelete(g, n)
    middle[1][n] += (time.time() - start_time-0.1)
    middle[2][n] += 1
    print("%s секунд" % (time.time() - start_time))

workbook = xl.Workbook('reverseDelete.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, 'матрица')
worksheet.write(0, 1, 'время сортировки')
worksheet.write(0, 2, 'обр удаление')
for i in range(2, paramparampam+1):
    worksheet.write(i-1, 0, i)
    worksheet.write(i-1, 1, middle[0][i]/(middle[2][i] if middle[2][i]!=0 else 1))
    worksheet.write(i-1, 2, middle[1][i]/(middle[2][i] if middle[2][i] != 0 else 1))
workbook.close()