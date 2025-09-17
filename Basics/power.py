def power(n,p):
    if p == 0:
        return 1
    else:
        return n*power(n,p-1)
    
    

n = int(input())
p = int(input())
print(power(n,p))