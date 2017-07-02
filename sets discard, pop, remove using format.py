n = int(input())
s = set(map(int, raw_input().split())) 
for i in range(int(raw_input())):
    eval('s.{0}({1})'.format(*raw_input().split()+['']))

print(sum(s))