'''The FIVE employees follow a strange convention. 
They will continue the meeting only if the following condition is satisfied.

The sum of the employee-ids of every pair of 
adjacent employees at the table must be an even number.

They are so lazy that they won't move around to satisfy the above condition. 
If the current seating plan doesn't satisfy the condition, the meeting will be canceled.
You are given the employee-id of all five employees. 
Your task is to decide if the meeting happened or not.'''
a = []
status = True
for i in range(5):
    i = int(input())
    a.append(i)
for i in range(len(a)-1):
    if (a[i] + a[(i+1)%5]) %2 != 0: #m%n = m if m<n
        status = False

if status:
    print("Yes")
else:
    print("No")
    
    