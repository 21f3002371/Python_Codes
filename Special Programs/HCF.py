num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
smaller = min(num1,num2)
for i in range(1,smaller+1):
    if (num1%i == 0) and (num2%i == 0):
        hcf = i
print(f'HCF of {num1} and {num2} is {hcf}')