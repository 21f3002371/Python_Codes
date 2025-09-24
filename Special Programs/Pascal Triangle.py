from math import factorial
rows = int(input('Enter the number of rows:'))
for i in range(rows):
    for j in range(1,rows-i):
        print(end= ' ')
    for k in range(i+1):
        print(int(factorial(i)/(factorial(k)*factorial(i-k))),end= ' ')
    print('')
    
        