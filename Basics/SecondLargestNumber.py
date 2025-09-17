a = [1,5,6,3,12,87,66,55,41]
def SecondLargestNumber(a):
    n = len(a)-1
    while n > 0:
        for i in range(n):
            if a[i]> a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
        n -= 1
    return a[-2]

for i in range(len(a)):
      if a[i] == SecondLargestNumber(a):
          print(f'index is at {i} index and number is {a[i]}')