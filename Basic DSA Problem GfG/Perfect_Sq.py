# Tip: the nth square number is sum of n odd numbers
import math as mt
def PerfectSq(n):
    if mt.ceil(mt.sqrt(n)) == mt.floor(mt.sqrt(n)):
        return True
    else:
        return False
    
n = int(input("Enter the Number: "))
if PerfectSq(n):
    print("Yes, perfect square")
else:
    print("Not a perfect square")    
     