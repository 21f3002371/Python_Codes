vowels = ['a','e','i','o','u']
s = input("Enter the word: ")
s = s.replace(" ","").lower()
count = 0
for i in s:
    if i in vowels:
        count += 1
        
print(count)