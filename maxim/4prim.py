INF = 9999999

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
        print(str(x) + "->" + str(y) + ": " + str(g[x][y]))
        pusto[y] = 1

n = 5
g = [[0, 2, 3, 0, 0],
     [2, 0, 4, 8, 0],
     [3, 4, 0, 9, 5],
     [0, 8, 9, 0, 7],
     [0, 0, 5, 7, 0]]

prim(n, g)
