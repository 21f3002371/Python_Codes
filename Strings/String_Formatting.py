name = 'Utkarsh'
city = 'Varanasi'
print("My name is %s" %(name))
print("My name is %s and I am currently in %s." %(name,city))
print("My name is {1} and I live in {0}".format(name,city))

# An integer can be provided in place of float
print("I got {0:.3f}% marks in English".format(55))

print(f"So we are in {city}")
print(f"So we are in {city.upper()}") #UPPERCASE

print(f"""We are in {city} \n
       I am {name}""")

x = 10
y = 20
print(f"The result of {{x+y}} is {{{x+y}}}")