'''Accept a positive integer n as input and print the sum of all prime numbers in the range [1,n].
endpoints inclusive. If there are no prime numbers in the given range, then print 0.
'''
sum = 0

n = int(input())
def prime(number):
    status = True
    for i in range(2,number):
        if number%i == 0:
            status = False
            break
    return status

for j in range(2,n+1):
    if prime(j):
        sum += j
        
print(sum)
