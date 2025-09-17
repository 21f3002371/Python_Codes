
def function(n):
    sum = 0
    product = 1
    for i in n:
        sum += i
        product *= i
    return sum, product
    
a = [1,2,3,4,5]
print(function(a))