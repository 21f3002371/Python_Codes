# no. of whitespaces before the first star = no. of rows - row number
rows = int(input('Enter number of rows:'))
for i in range(1,rows+1):
    for space in range(1,rows-i+1): #White space = rows - row number
        print(end= " ")
    for star in range(1,i+1): #Printing stars
        print('*',end= ' ')
    print('') #For coming to next line