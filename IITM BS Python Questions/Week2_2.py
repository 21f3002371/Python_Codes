'''A sequence of five words is called magical if the ith word is a substring of the  (i + 1)th word 
for every  i in range 1<= i < 5
Accept a sequence of five words as input, one word on each line. 
Print magical if the sequence is magical and non-magical otherwise.

Note that str_1 is a substring of str_2 
if and only if str_1 is present as a sequence of consecutive characters in str_2.'''
list1 = []
status = True
for i in range(5):
     s = input()
     list1.append(s)

for i in range(len(list1)-1):
    if list1[i] not in list1[i+1]:
        status = False
        break
if status:
    print("Magical")
else:
    print("Not Magical")
     