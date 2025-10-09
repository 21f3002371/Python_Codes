def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter the number: "))

for i in range(2, number + 1):
    if isprime(i):
        while number % i == 0: 
            #100%2 = 0  so store2, 50%2 = 0 so store 2
            #25%2  != 0 so iterate further 
            # This same will happen for 5 and 
            # prime factorization = 2*2*5*
            print(i)
            number //= i

        