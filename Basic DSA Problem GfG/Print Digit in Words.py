# Using Dictionary
def PrintNum(N):
    digit = {'1' : 'One', '2' : 'Two', '3' : 'Three', '4' : 'Four', '5': 'Five', 
             '6': 'Six', '7' : 'Seven', '8': 'Eight', '9': 'Nine', '0': 'Zero'}
    for i in N:
        print(digit[i], end = ' ')
n = input('Enter the Number: ')
PrintNum(n)