list1 = [1,4,78,90,87,12,33]
max = list1[0]
for i in range(len(list1)):
    if list1[i] > max:
        max = list1[i]
secondlargest = list1[0]      
for j in range(len(list1)):
    if list1[j] > secondlargest and list1[j] != max:
       secondlargest = list1[j]
        
print(secondlargest)