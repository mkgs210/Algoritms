def sorte(d):
    d = list(d.items())
    d.sort(key=lambda i: i[1])
    return d


def vid(n, g): #new dict with edge of graph
    d = {}
    letters = [*'abcdefghijklmnopqrstuvwxyz'[:n]]
    for i in range(n):
        for j in range(n):
            if g[i][j] == 0:
                continue
            if letters[i]+letters[j] not in d and letters[j]+letters[i] not in d:
                d |= {letters[i]+letters[j]:g[i][j]}
    return d


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
    for i in range(0, len(pusto), 2):
        print(pusto[i][0], ' -> ', pusto[i][1], ': ', pusto[i+1])

n = 5
g = [[0, 2, 3, 0, 0],
     [2, 0, 4, 8, 0],
     [3, 4, 0, 9, 5],
     [0, 8, 9, 0, 7],
     [0, 0, 5, 7, 0]]
g = vid(n,g)
g = sorte(g)
kraskal(g)
