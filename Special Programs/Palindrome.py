s = input('Enter the string: ')
s.replace(" ","").lower()
start  = 0
end = len(s)-1
flag = False
while start < end:
    if s[start] == s[end]:
        
         flag = True
    start += 1
    end -= 1
if flag == True:
    print('Palindrome')
else: 
    print('Not a Palindrome')
    