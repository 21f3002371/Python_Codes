s = input("Enter the Sentence: ").split(" ").lower() #.split converts into list
word = input("Enter the word searching for: ").lower()
print(s)
if word in s:
    print("Yes, it is present")
else:
    print("No, it is not present")