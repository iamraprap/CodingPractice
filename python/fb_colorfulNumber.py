from functools import reduce

def productOfString(A):
    a = int(A[0])
    for b in range(1, len(A)):
        a *= int(A[b])
    return a


def colorful(A):
    B = str(A)
    n = len(B)
    z = 0
    prod = set([int(i) for i in B])
    if n!=len(prod):
        return 0
    for i in range(z, n):
        for j in range(i+2,n+1):
            pos = reduce(lambda x, y : int(x)*int(y), B[i:j] ) #productOfString(B[i:j])
            if pos in prod:
                return 0
            prod.add(pos)
    return 1
print(colorful(12)==0)
print(colorful(99)==0)    
print(colorful(23)==1)
print(colorful(123)==0)