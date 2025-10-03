'''You are given the dates of birth of two persons, 
not necessarily from the same family. 
Your task is to find the younger of the two. 
If both of them share the same date of birth, 
then the younger of the two is assumed to be that person 
whose name comes first in alphabetical order.
The input will have four lines. 
The first two lines correspond to the first person, 
while the last two lines correspond to the second person.
For each person, the first line corresponds to the name and 
the second line corresponds to the date of birth in DD-MM-YYYY format. 
Your output should be the name of the younger of the two.'''

name1, date1, name2, date2 = input(),input(), input(), input()

if int(date1[6:10]) > int(date2[6:10]):
    print(name1)
elif int(date1[6:10]) < int(date2[6:10]):
    print(name2)
else:
    if int(date1[3:5]) > int(date2[3:5]):
        print(name1)
    elif int(date1[3:5]) < int(date2[3:5]):
        print(name2)
    else:
        if int(date1[:2]) > int(date2[:2]):
            print(name1)
        elif int(date1[:2]) < int(date2[:2]):
            print(name2)
        else:
          print(min(name1,name2))