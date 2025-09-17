# name[start_index:end_index] - character of end index is not included
a = 'Hello'
print(a[1:4]) #ell
print(a[:len(a)+1]) #No need to specify start index
print(a[0-len(a):]) # No need to specify end index