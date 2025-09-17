a = int(input("Enter A"))
b = int(input("Enter B"))
temp = a
a = b
b = temp
print(a,b)

#Another way
c = int(input("Enter C"))
d = int(input("Enter D"))

c = c+d 
d = c-d
c = c-d
print(c,end = ' ')
print(d)

# One more way is doing XOR Gate

#rot_Two in python
# a,b = b,a