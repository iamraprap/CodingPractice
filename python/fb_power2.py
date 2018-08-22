def isPower(A):
    if A == 1:
        return True
    for h in xrange(2, int(A**0.5)+1):
        for i in xrange(2, 32):
            if A==h**i:
                return True
    return False

print(isPower(3125)==1)
print(isPower(2048)==1)
print(isPower(16)==1)
print(isPower(4)==1)
print(isPower(4294967296)==0)

'''
3125
1
2048
1
16
1
4
1
0
1
4294967296
0
16808
0
16384
1
'''