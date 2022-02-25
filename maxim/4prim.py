import time, random
import xlsxwriter as xl
INF = 9999999
how_many = 50
how_many2 = 150
paramparampam = how_many2+1

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

n=1
middle = [[0 for i in range(paramparampam+1)]for j in range(2)]
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
        middle[0][n] += (time.perf_counter() - start_time)
        middle[1][n] += 1
        '''file.write(str(n))
        file.write(' ' + str(time.time() - start_time-0.1) + '\n')'''
        print("%s секунд" % (time.perf_counter() - start_time))

'''file.close()'''
workbook = xl.Workbook('prim.xlsx')
worksheet = workbook.add_worksheet()
for i in range(2, paramparampam+1):
    worksheet.write(i-2, 0, i)
    worksheet.write(i-2, 1, middle[0][i]/(middle[1][i] if middle[1][i]!=0 else 1))
workbook.close()
