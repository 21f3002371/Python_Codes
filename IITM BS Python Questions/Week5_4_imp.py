n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Row sums
row_sum = [sum(row) for row in matrix]

# Column sums (zip(*matrix) transposes the matrix)
column_sum = [sum(col) for col in zip(*matrix)]

# Diagonal sums
diagonal_1 = sum(matrix[i][i] for i in range(n))
diagonal_2 = sum(matrix[i][n - i - 1] for i in range(n))

# Check if all sums are equal
if (len(set(row_sum + column_sum + [diagonal_1, diagonal_2])) == 1):
    print("Magical")
else:
    print("Not Magical")
    
    
'''A n*n square matrix of positive integers 
is called a magic square if the following sums are equal:
(1) row-sum: sum of numbers in every row; there are 
n such values, one for each row
(2) column-sum: sum of numbers in every column; there are 
n such values, one for each column
(3) diagonal-sum: sum of numbers in both the diagonals; 
there are two values
n = int(input())
matrix = []
for i in range(n):
    val = list(map(int,input().split()))
    matrix.append(val)
row_sum = []  
column_sum = []
diagonal_1 = []
diagonal_2 = []
for i in range(len(matrix)):
    sum = 0
    for j in range(len(matrix[i])):
            sum += matrix[i][j]
    row_sum.append(sum)
for i in range(len(matrix)):
    sum = 0
    for j in range(len(matrix[i])):
            sum += matrix[j][i]
    column_sum.append(sum)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            diagonal_1.append(matrix[i][j])
for i in range(len(matrix)):
      diagonal_2.append(matrix[i][n - i - 1])
      
row1,column1 = row_sum[0],column_sum[0]
for i in range(1,len(row_sum)):
    if row_sum[i] == row1 and column_sum[i] == column1:
        status1 =True
    else:
        status1 = False   
        
if sum(diagonal_1) == sum(diagonal_2):
    status2 = True
    
if status1 and status2:
    print("Magical")   
else:
    print("Not Magical")  '''        