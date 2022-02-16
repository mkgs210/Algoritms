def iterativeFact(n):
    r = 1
    for i in range(n):
        r = r*n
        n -= 1
    return r

def recursiveFact(n):
    if n == 0:
        return 1
    else:
        return n*recursiveFact(n-1)

def iterativeFib(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    r, k = 1, 1
    for i in range(2, n):
        r = r+k
        r, k = k, r
    return k

def recursiveFib(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursiveFib(n-2)+recursiveFib(n-1)

def iterativeTrib(n):
    if n==0:
        return 0
    elif n == 1 or n == 2:
        return 1
    k0=0; k1=1; k2=1
    for i in range(2, n):
        k0 = k0+k1+k2
        k0, k1, k2 = k1, k2, k0
    return k2

def recursiveTrib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return recursiveTrib(n-1)+recursiveTrib(n-2)+recursiveTrib(n-3)


def input_n():
    print('take a non-negative integer number')
    n = input()
    if n.isdigit() and int(n)>=0:
        return int(n)
    else:
        print('unacceptable value')
        input_n()

n = input_n()

print('iterative factorial', iterativeFact(n))
print('recursive factorial', recursiveFact(n))

print('iterative fibonachi', iterativeFib(n))
print('recursive fibonachi', recursiveFib(n))

print('iterative tribonachi', iterativeTrib(n))
print('recursive tribonachi', recursiveTrib(n))
