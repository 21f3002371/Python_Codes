n = input("Enter the number: ")
sum = 0
length = len(n)
for i in range(length):
    sum += int(n[i])
    
print(f"The sum of digits of {n} is {sum}")