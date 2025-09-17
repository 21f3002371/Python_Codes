n = int(input())
limit = int(input())
for i in range(1,n+1):
    if i == limit:
        break
    if i%2 == 0:
        continue
    print(i)
# When there is nothing to write in if, while loops just write 'pass'
# to leave that place for a while