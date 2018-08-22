
'''
  1 1 2 3 4
  1 2 3 4 2
  1 1 2 3 4 
  3 2 4 1 3
  4 1 3 2 1
'''
n = 5
matrix = [
              [1, 1, 2, 3, 4]
            , [1, 2, 3, 4, 2]
            , [1, 1, 2, 3, 4]
            , [3, 2, 4, 1, 3]
            , [4, 1, 3, 2, 1]
        ]



visited = {}
maxScore = -1
'''
recursive

def getScore(x, y, group, score):
    global n, matrix, visited
    # traverse the neigbors DFS by starting at top left corner of a starting point
    for i in range(max(0, x-1), min(x+2, n)):
        for j in range(max(0, y-1), min(y+2, n)):
            if (i,j) in visited.keys(): # check if it is visited
                continue            
            else:
                visited[i, j] = matrix[i][j]
            if matrix[i][j]==group:
                score = getScore(i, j, group, score) + 1
    return score
'''
def getScore(x, y, group, score):
    global n, matrix, visited
    # traverse the neigbors DFS by starting at top left corner of a starting point
    for i in range(max(0, x-1), min(x+2, n)):
        for j in range(max(0, y-1), min(y+2, n)):
            if (i,j) in visited.keys(): # check if it is visited
                continue            
            else:
                visited[i, j] = matrix[i][j]
            if matrix[i][j]==group:
                score = getScore(i, j, group, score) + 1
    return score

for x in range(n):
    for y in range(len(matrix[x])):
        if (x,y) in visited.keys():
            continue
        else:
            visited[x, y] = matrix[x][y]
        score = getScore(x, y, matrix[x][y], 1) # by DFS get the score
        maxScore = max(maxScore, score) # store the maxScore
print(maxScore)
        


        # 0, 0 = 1
        # 0, 1 = 1
        # 1, 0 = 1
        # 2, 0 = 1
        # 2, 1 = 1

