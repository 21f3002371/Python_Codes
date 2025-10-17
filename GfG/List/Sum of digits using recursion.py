def sumdigit(n):
    if n < 10:
        return n
    return sumdigit(n//10) + n%10

n = int(input())
print(sumdigit(n))