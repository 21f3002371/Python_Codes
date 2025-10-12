'''Write a function named is_perfect that accepts 
a positive integer n
as argument and returns True if it is perfect, 
and False otherwise.'''
# 6 = 1+2+3
def perfect(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
            
    if n == sum:
        return True

num = int(input())
if perfect(num):
    print(f'{num} is perfect')
else:
    print(f'{num} is not perfect')