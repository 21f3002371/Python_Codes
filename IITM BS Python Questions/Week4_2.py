'''Accept a sequence of comma-separated words as input. 
Reverse the sequence and print it as output.'''

s = input().split(',')
for j in range(len(s)-1,-1,-1):
    if j!= 0:
        print(s[j],end=",")
    else:
        print(s[0])
'''
s = input().split(',')
print(','.join(s[::-1]))
'''