'''Accept two positions as input: start and end. 
Print YES if a bishop at start can move to end in exactly one move.
Print NO otherwise. Note that a bishop can only move along diagonals.
'''
start , end = input().upper(), input().upper()
# start would be a1, end would be c3 like that
pos = 'ABCDEFGH' # total 8 positions
# Now we need 4 parameters for finding absolute difference
start_vert , start_hor = pos.index(start[0]), int(start[1])
end_vert, end_hor = pos.index(end[0]), int(end[1])

if abs(start_vert - end_vert) == abs(start_hor - end_hor):
    print('yes')
else:
    print('no')