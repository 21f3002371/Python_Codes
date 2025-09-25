#To check armstrong number of n-digit number
num = int(input('Enter a n-digit number:'))
temp1 = num
digit_length = 0

#To find the length of the digit
while temp1 > 0:
    digit_length += 1
    temp1 //= 10
    
# Main loop for checking Armstrong Number
sum = 0
temp2 = num
while temp2 > 0:
    digit = temp2%10
    sum += digit**digit_length
    temp2 //= 10

# Final Check if Number equal to Sum
if num == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong number")