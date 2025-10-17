# Palindrome using recursion
def palindromerec(s):
    n = len(s)
    if n == 0  or n == 1:
           return True
    if s[0] == s[n-1]:
        return palindromerec(s[1:-1])
    return False    
        
        

s = input().lower()
if palindromerec(s):
    print('Yes')
else:
    print('No')
    
    