# (1^2 + 2^2 + ... + n^2) - (1 + 2 + ... + n)^2

def Square_Diff(n):

    l = (n * (n + 1) * (2 * n + 1)) / 6
    
    k = (n * (n + 1)) / 2

    k = k ** 2
    m = abs(l - k)
    return int(m)
number = int(input("Enter the number"))
print(Square_Diff(number))