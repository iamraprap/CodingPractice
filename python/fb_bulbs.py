
def bulbs(A):
    flipCtr = 0
    ctr = 0
    for i in A:
        #apply past flips
        if flipCtr %2 == 1:
            i = int(not i)

        if i == 1:
            continue

        i = int(not i)
        flipCtr += 1
        ctr+=1
    return ctr

print("%s" % (bulbs([1, 0, 1, 1, 1])==2))
print("%s" % (bulbs([1, 1, 1, 1, 1])==0))
print("%s" % (bulbs([1, 0, 1, 0, 1])==4))
print("%s" % (bulbs([1, 0, 1, 0, 0])==3))
print("%s" % (bulbs([1, 0, 1, 0, 1, 0, 1, 1])==6))
