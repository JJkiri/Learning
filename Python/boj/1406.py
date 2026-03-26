#1406 

import sys

input = lambda: sys.stdin.readline().rstrip('\n') # use input more fast & dont need to change 

word = input()

m = int(input())

left_stack = []
right_stack = []

for i in word: #make left stack
    left_stack.append(i)

for i in range(m):
    cmd = input()
    if cmd == 'L' and left_stack:
        right_stack.append(left_stack.pop())
        # left pop, right append
    elif cmd == 'D' and right_stack:
        left_stack.append(right_stack.pop())
        # right pop, left append
    elif cmd == 'B' and left_stack: #left pop, no append
        left_stack.pop()
    elif cmd[0] == 'P': #P, left append(x)
        left_stack.append(cmd[2]) # P y >> x[0] = P // x[2] = y or split)_

print(''.join(left_stack+right_stack[::-1])) ## ''join(+) use '+' and stack[::-1]?