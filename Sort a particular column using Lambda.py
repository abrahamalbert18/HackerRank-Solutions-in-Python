# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M =map(int, raw_input().split())
sample= [ map(int, raw_input().split()) for i in range(N)]
k=input()
sample.sort(key=lambda x: x[k])
for i in sample:
    print " ".join(map(str,i))

    
