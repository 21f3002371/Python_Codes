# Using loop
A = ['I','am','Utkarsh','Hello','World','America','Utkarsh']
longest = ""
for name in A:
    if len(name) > len(longest):
       longest = name
print(longest)
# Using Dictionary
length_dict = {}
for name in A:
    if len(name) in length_dict:
         length_dict[len(name)] += " , " + name
    else:
          length_dict[len(name)] = name
print(length_dict)
print(max(length_dict))
    
