matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
result=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        result[i][j]=matrix[i][j]
        
for r in result:
    print (r)