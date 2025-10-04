'''find all solutions of 
x^2 + y^2 = z^2 
provided x < y < z < n
Provide the answers in triplet form (x,y,z)
'''
status = False
n = int(input('Enter the number: '))
for x in range(1,n):
    for y in range(1+x,n):
        for z in range(1+y,n):
            if x**2 + y**2 == z**2:
                status = True
                print(f'{x},{y},{z}')
                
                
if not status:
    print('No Solution')   
            