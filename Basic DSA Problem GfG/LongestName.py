A = ['I','am','Utkarsh','Hello','World','America','Utkarsh']

# Using loop
'''longest = ""
for name in A:
    if len(name) > len(longest):
       longest = name
print(longest)'''

# Using Dictionary
# A Dictionary cannot store multiple item in a single key. 
# To store mutliple items to akey, use list
length_dict = {}

for name in A:
    if len(name) not in length_dict:
          length_dict[len(name)] = [name]
         
    else:
          length_dict[len(name)].append(name)
print(length_dict)
print(max(length_dict))
    
