'''Accept a string as input, convert it to lower case, sort the string in alphabetical order, 
and print the sorted string to the console.
You can assume that the string will only contain letters.'''
import string
s = input().lower()
new =''
for i in string.ascii_lowercase:
    for j in range(0,len(s)):
        if i == s[j]:
             new += i
        
print(new)