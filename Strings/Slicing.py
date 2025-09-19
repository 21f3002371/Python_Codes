# name[start_index:end_index] - character of end index is not included
a = 'Hello'
print(a[1:4]) #ell
print(a[:len(a)+1]) #No need to specify start index
print(a[0:]) # No need to specify end index

s = 'I am Utkarsh'
print(s[0::2])
print(s[::2]) #Accessing the entire string

# Negative Parameter : Backward Reading #Reversing a string
print(s[-1::-1])
# OR
print(s[::-1])