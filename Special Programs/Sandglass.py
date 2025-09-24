row = int(input('Enter the number of rows:'))
#Pattern 1
for i in range(row,0,-1):
    for j in range(1,row-i+1):
       print(end= ' ')
    for j in range(1,i+1):
       print("*", end = ' ')
    print('')
#Pattern 2
for i in range(1,row+1):
    for m in range(1,row-i+1):
        print(end=" ")
    for q in range(1,i+1):
        print("*",end = " ")
    print('')
    
