#To check armstrong number of three digit number
num = int(input('Enter a n-digit number:'))
digit = num
digit_length = 0
while digit > 0:
    digit_length += 1
    digit //= 10
sum = 0
temp = num
while temp > 0:
    digit = temp%10
    sum += digit**digit_length
    temp //= 10
if num == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong number")