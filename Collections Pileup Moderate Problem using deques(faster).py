# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

def stackable(cubes):
    curr = cubes.popleft() if cubes[0] > cubes[-1] else cubes.pop()
    while cubes:
        left, right = cubes[0], cubes[-1]
        if left >= right and left <= curr:
            curr = cubes.popleft()
        elif right > left and right <= curr:
            curr = cubes.pop()
        else:
            return False
    return True

for i in range(int(raw_input())):
    n, cubes = input(), deque(map(int, raw_input().split()))
    print('Yes' if stackable(cubes) else 'No') 