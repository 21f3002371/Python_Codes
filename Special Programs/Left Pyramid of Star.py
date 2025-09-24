row = int(input('Enter the Number of Rows: '))
# No. of white Spaces = Total Row - i row
for i in range(1,row+1):
    for j in range(1,row-i+1):
        print(end = ' ')
    for k in range(1,i+1):
        print('*', end='')
    print('')
for q in range(1,row+1):
    for t in range(1,q+1):
        print(end = ' ')
    for m in range(1,row-q+1):
        print('*',end='')
    print('')
    