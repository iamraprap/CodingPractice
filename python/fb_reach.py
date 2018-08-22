'''
x 4 3 4 5 3
y 4 4 -2 1 3
11
1 -2
1 7
0
'''
'''
def coverPoints(X, Y):
    if len(X)==1 and len(Y)==1:
        return 0

    j = X[0]
    totX = 0
    for i in range(1, len(X)):
        totX+=abs(j-X[i])
    j = Y[0]
    totY = 0
    for i in range(1, len(Y)):
        totY+=abs(j-Y[i])
    return max(totX, totY)
#coverPoints([-2], [7])
'''
def coverPoints(X, Y):
    steps = 0
    for i in range(0, len(X)-1):
        steps += max(abs(X[i+1]-X[i]),abs(Y[i+1]-Y[i]))
    return steps

print(coverPoints([3, 4, 5, 3], [4, -2, 1, 3]))