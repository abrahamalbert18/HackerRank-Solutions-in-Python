import sys

stack = []
max_items = []

N = int(sys.stdin.readline())
for i in xrange(0, N):
    query = sys.stdin.readline().split()
    if query[0] == "1":
        x = int(query[1])
        stack.append(x)
        if len(max_items) == 0 or x >= max_items[len(max_items) - 1]:
            max_items.append(x)
    elif query[0] == "2":
        x = stack.pop()
        if max_items[len(max_items) - 1] == x:
            max_items.pop()
    else: # query[0] == "3"
        print(max_items[len(max_items) - 1])