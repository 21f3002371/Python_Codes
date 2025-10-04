'''
Accept a phone number as input. A valid phone number should satisfy the following constraints.

(1) The number should start with one of these digits: 6, 7, 8, 9

(2) The number should be exactly 10 digits long.

(3) No digit should appear more than 7 times in the number.

(4) No digit should appear more than 5 times in a row in the number.
If the fourth condition is not very clear, then consider this example: 
the number 9888888765 is invalid because the digit 8 appears more than 5 times in a row.

Print the string valid if the phone number is valid. If not, print the string invalid.'''

ph = input()

status = True
for d in ph:
    if ph.count(d) > 7:
        status = False
for i in range(len(ph)):
    if 6*ph[i] in ph:
        status = False #checking if a 6time string is in number or not 
if ph[0] in '6789' and len(ph) == 10 and status:
    print("Valid")
else:
    print("Invalid")