#Escape character is used to insert a non-allowed character in a string
# \non-allowed-character

print("Hello \"Utkarsh\"")

#\n - newline  #\\ - include \ in string
#\b- backspace #\ooo - include octal
#\t - tab      #\xhh - include hexa-decimal
print("Hell\bo In")

#String Formatting - %
# %d - deciaml/integer
# %c - character
# %s - string
# %f - float value
n = int(input('Enter the age'))
print("Age of that person is %d" %(n))