def diagonal(a):
    n = len(a)
    res = [[] for _ in range(2*n-1)] 
    for i in range(n):
        for j in range(n):
            res[i+j].append(a[i][j])
    return res

    '''
    return [[a[row][col-row]
                for row in range(col + 1) if 0 <= row < size and 0 <= col-row < size]
                for col in range(size * 2 - 1)]
0,0
0,1 - 1,0
0,2 - 1,1, 1,0

1,2 - 2,1

2,2
'''

print("%s"  %  str(   diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])    ) ) 
