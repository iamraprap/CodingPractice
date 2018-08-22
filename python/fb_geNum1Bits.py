import math
def numSetBits(A):
    ctr = 0
    while A>0:
        A -= 2 ** math.floor(math.log(A)/math.log(2))
        ctr+=1
    return ctr
'''
def numSetBits(self, A):
    ret = 0
    while A != 0:
        if A&1:
            ret += 1
        A = A >> 1
    return ret
'''
print(numSetBits(0)==0)
print(numSetBits(1)==1)
print(numSetBits(2)==1)
print(numSetBits(3)==2)
print(numSetBits(4)==1)
print(numSetBits(8)==1)
print(numSetBits(11)==3)
print(numSetBits(12)==2)
print(numSetBits(13)==3)
print(numSetBits(14)==3)
'''
print(numSetBits(4294967294)==31)
print(numSetBits(4294967295)==32)
