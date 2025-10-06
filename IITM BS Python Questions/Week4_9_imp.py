'''You are given the names and dates of birth of a group of people. 
Find all pairs of members who share a common date of birth. 
Note that this date need not be common across all pairs.
It is sufficient if both members in a pair have the same date of birth.

The first line of input is a sequence of comma-separated names. 
The second line of input is a sequence of comma-separated positive integers. 
Each integer in the sequence will be in the range

Find all pairs of names that share a common date of birth and store 
them in a list called common. 
Each element of this list is itself a list, and should be of the form [name1, name2], 
such that name1 comes before name2 in alphabetical order.

sachin,ramesh,rohit,priya,saina,sandeep,stella
100,50,100,20,30,20,20
Your list common could look like this:

[['rohit', 'sachin'], ['priya', 'sandeep'], ['priya', 'stella'], ['sandeep', 'stella']]
'''
s = input().split(',')
date = input().split(',')
d = {}
for i in range(len(date)):
    if date[i] in d:
        d[date[i]].append(s[i])
    else:
        d[date[i]] = [s[i]]
print(d)
print(d.values())

#Common List
common = []
for names in d.values():
    if len(names) > 1:
        names.sort()
        for i in range(len(names)):
            for j in range(i+1, len(names)):
                common.append([names[i], names[j]])
                
print(common)

