# Find LCM of two numbers
n1,n2 = map(int,input().split()) # For outputs like '1 2 3'
r = max(n1,n2)
while True:
    if (r%n1) == 0 and (r%n2) == 0:
        print(f'LCM of {n1} and {n2} is {r}')
        break
    r += 1
    
    
        