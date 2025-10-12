'''The distance between two letters in
the English alphabet is one more than the number of 
letters between them. 
Alternatively, it can be defined as the number of 
steps needed to move from the alphabetically smaller letter to
the larger letter. This is always a non-negative integer.'''

# d(dog,cat) = d(d,c) + d(a,o) + d(g,t)
# return -1 if words are of unequal length
from string import *
def distance(x,y):
     lower_letters = ascii_lowercase
     if x > y:
         start = lower_letters.find(y)
         end = lower_letters.find(x)
     elif x < y:
         start = lower_letters.find(x)
         end = lower_letters.find(y)
     else:
         start = 0
         end = 0
        
     return len(lower_letters[start:end])
length = 0
x,y = input().lower(),input().lower()
for i in range(len(x)):
    if len(x) != len(y):
        length = -1
    else:
        length += distance(x[i],y[i])
    
print(length)
    
