# Shorter syntax of creating a new list from existing one
names = ['John','Utkarsh']
u_names = [i for i in names if 'U' in i]
print(u_names)

# Syntax = [expression for item in iterable if condition == True]

list = [i for i in range(6) if i%2 == 0]

animals = ['lion','tiger','monkey','elephant','frog']
fil_animals = [i.title() for i in animals ]
print(fil_animals)