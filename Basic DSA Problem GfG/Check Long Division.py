def DivisiblebySix(n):
    T1 = False
    T2 = False
    length = len(n)
    if (((int)(n[-1]))%2) == 0:
        T1 = True
    a = [int(n[i]) for i in range(length)]
    sum = 0
    for j in a:
        sum += j
    if sum% 3 == 0:
        T2 = True
    if T1 and T2:
        return True
    else:
        return False
    
n = input("Enter the Number: ")
if DivisiblebySix(n):
    print("Yes, divisible by six")
else:
    print("No, Not divisible by six")