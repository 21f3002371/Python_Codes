'''Accept two strings as input and form a new string by 
removing all characters from the second string which are present in the first string. 
Print this new string as output. 
You can assume that all input strings will be in lower case.'''
s1,s2 = input(),input()
new = ''
for i in s2:
    if i not in s1:
        new += i
print(new)