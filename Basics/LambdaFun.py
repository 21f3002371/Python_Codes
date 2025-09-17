# Anonymous Functions are called Lambda
f = lambda x,y : (x+y)*(x-y)
print(f(10,10))

# Using Filter along with lambda
# filter takes two arguements - filter(function,iterable)
A = []
n = int(input("Enter range of number"))
for i in range(1,n+1):
    A.append(i)
    
only_even = list(filter(lambda n :n%2 == 0,A))

print("List with even numbers for range n",only_even)

#Maping Function
# It maps to each iteral
#Like for adding a constant to each item in a list, we can use that method

add_two = list(map(lambda n: n+2,only_even))
print("doubling the even numbers",add_two)