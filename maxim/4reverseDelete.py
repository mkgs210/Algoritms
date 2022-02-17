def sorte(d):
    d = list(d.items())
    d.sort(key=lambda i: -i[1])
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


def reverseDelete(d, n):
    pusto = []
    letters = ','.join([i[0] for i in d])
    while(len(d)>=n):
        if letters.count(d[0][0][0])<2 or letters.count(d[0][0][1])<2:
            letters = letters.replace(d[0][0], '')
            d = d[1:]+[d[0]]
            continue
        letters = letters.replace(d[0][0], '')
        d = d[1:]
    d.sort()            #для красоты
    for i in d:
        print(i[0][0], ' -> ', i[0][1], ': ', i[1])

n = 5
g = [[0, 2, 3, 0, 0],
     [2, 0, 4, 8, 0],
     [3, 4, 0, 9, 5],
     [0, 8, 9, 0, 7],
     [0, 0, 5, 7, 0]]
g = vid(n,g)
g = sorte(g)
print(g)
reverseDelete(g, n)
