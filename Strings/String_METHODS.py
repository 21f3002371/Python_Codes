# 1) .strip() Method : Remove characters which r leading n trailing
'''print("######Hello World#####".strip("#"))
print(" ###Hello World".strip('#'))
print("Hello World".strip('ldoH'))'''
# 2) .lstrip() : Removes the leading characters only
# 3) .rstrip() : Removes the right characters
# 4) .split() : Use to split a string into a list - Syntax : .split(separator(position), maxsplit(maximum split))
'''s = "Hello My name is Utkarsh Mishra"
print(s.split(' ', maxsplit = 2)) #Take two white spaces and divide it into 3 parts'''
# 5) .rsplit() - is sameas split but do spliting from right
'''print("Hello My name is Utkarsh Mishra".rsplit(" ", maxsplit = 2))'''

# 6) separator.join()- Join the elements of an iterable of 'string'
'''l1 = ['Hi', 'I am', 'Utkarsh']
print(' '.join(l1))
d = {'name':'Adam', 'country': 'US'}
print(' and '.join(d)) # Only keys of dictionary will get add'''
# 7) .replace() -Replace a string with another string - Syntax : .replace(oldstring, newString, count)
'''s  = 'I love to eat Mangoes & Mangoes only!'
print(s.replace('Mangoes', 'Pineapple',1))'''
# 8) .upper()- Uppercase, .lower() - lowercase, .capitalize() - first character is uppercase and rest are lowercase
'''print("maruti suzuki".capitalize())'''
# 9) .isupper() returns True if all characters are uppercase and vice versa for .islower()

# 10) .isalpha(): True if all characters are alphabet
# 11) .isnumeric(): True if all characters are numbers (.,/,-,* are not operators in string so return False)
# 12) .isalnum(): True if all characters are alphanumeric
'''print("utkarshmishra7503@gmail.com".isalnum()) # Returns False '''

# 13) .count(): Finds the number of occurrences of a substring in a given string Syntax: count(sub,start,end)
print(("Hello Halo! Namaste"*5).count('Halo!'))
# 14) .find(): Returns the index of the first occurrence of the substring Syntax : find(sub,string,end)
print("Hello Dear Utkarsh".find('U'))















