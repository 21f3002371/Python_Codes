n = int(input())
limit = 10
for i in range(1,n+1):
    if i == limit:
        print("Limit Reached")
        break
    if i%2 == 0:
        print("Yes",i)
    else:
        print("No",i)