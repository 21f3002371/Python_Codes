'''A bot starts at origin (0,0) and can make the following moves:
(1) UP
(2) DOWN
(3) LEFT
(4) RIGHT
Each move has a magnitude of 1 unit. Accept the sequence of moves made by the bot as input. 
The first entry in the sequence is always START while the last entry in the sequence is always STOP. 
A sample sequence is given below:
START
UP
RIGHT
LEFT
LEFT
DOWN
UP
STOP

Print the Manhattan distance of the bot from the origin. If the bot is at the position (x,y)
Manhattan = |x| + |y| from origin '''

seq = input()
x,y = 0,0 
while seq != 'STOP':
    if seq == 'UP':
        y += 1
    if seq == 'DOWN':
        y -= 1
    if seq == 'LEFT':
        x -= 1
    if seq == 'RIGHT':
        x+= 1
    seq = input()
print(abs(x) + abs(y))
