matrix=[[1,2,3],[4,0,6],[7,8,9]]

#brute force
m=len(matrix)
n=len(matrix[0])

for i in range(m):
    for j in range(n):
        if matrix[i][j]==0:
            #entire row to -1
            for k in range(n):
                if matrix[i][k]!=0:
                    matrix[i][k]=-1
            #entire column to -1
            for l in range(m):
                if matrix[l][j]!=0:
                    matrix[l][j]=-1

#replace -1 with 0
for i in range(m):
    for j in range(n):
        if matrix[i][j]==-1:
            matrix[i][j]=0
print(matrix)

#TC =O(m*n*(m+n))

#better approach
matrix1=[[1,2,3],[4,0,6],[7,8,9]]
m=len(matrix1)
n=len(matrix1[0])
row=[0]*m
col=[0]*n
#marking the rows and columns which have 0
for i in range(m):
    for j in range(n):
        if matrix1[i][j]==0:
            row[i]=1
            col[j]=1
#marking the rows and columns with 0
for i in range(m):
    for j in range(n):
        if row[i]==1 or col[j]==1:
            matrix1[i][j]=0
print(matrix1)

#TC =O(m*n) SC=O(m+n)

#optimal approach
matrix2=[[1,2,3],[4,0,6],[7,8,9]]
m=len(matrix2)
n=len(matrix2[0])
row0=False
col0=False
#marking the first row and column with 0
for i in range(m):
    if matrix2[i][0]==0:
        col0=True
        break
for j in range(n):
    if matrix2[0][j]==0:
        row0=True
        break   

#marking the rows and columns with 0
for i in range(1,m):
    for j in range(1,n):
        if matrix2[i][j]==0:
            matrix2[i][0]=0
            matrix2[0][j]=0
#marking the rows and columns with 0
for i in range(1,m):    
    for j in range(1,n):
        if matrix2[i][0]==0 or matrix2[0][j]==0:
            matrix2[i][j]=0 
#marking the first row and column with 0
if row0:
    for j in range(n):
        matrix2[0][j]=0
if col0:
    for i in range(m):
        matrix2[i][0]=0
print(matrix2)

#TC =O(m*n) SC=O(1)