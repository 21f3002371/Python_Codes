matrix = [[2,3,4,6],[6,3,2,1],[6,12,89,76],[23,90,10,21],[0,99,11,16]]
row = len(matrix)
column = len(matrix[1])
max_element = -99999 #Very small number
for i in range(row):
    for j in range(column):
        if (matrix[i][j] > max_element):
            max_element = matrix[i][j]
            
print(max_element)