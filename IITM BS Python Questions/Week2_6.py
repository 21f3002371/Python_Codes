'''Accept a string as input and print the vowels present in the string in alphabetical order. 
If the string doesn't contain any vowels, then print the string none as output. 
Each vowel that appears in the input string — irrespective of its case — 
should appear just once in lower case in the output.'''
# Creating Dictionary of Vowels
vowel = {'a': 0 , 'e': 0, 'i': 0, 'o': 0, 'u': 0}
s = input().lower().split()
for j in s:
    for i in j:
        if i in vowel:
            vowel[i] +=1
print(vowel)
# Checking if all Dictionary key elements are zero or not
status = False
for i in vowel.values():
    if i != 0:
        status = True
present_vowels = [k for k in vowel if vowel[k] != 0]
if status:
    print("Yes vowels present", present_vowels)
    
else:
    print("No vowels present")
