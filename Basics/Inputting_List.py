def input_list(n):
    x = []
    for i in range(n+1):
        j = int(input())
        x.append(j)
        
    return x

n = int(input('Enter the length of list'))
print(input_list(n))