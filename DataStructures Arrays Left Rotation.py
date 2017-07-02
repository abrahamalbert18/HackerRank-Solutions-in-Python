n,d = map(int,raw_input().split())
array=map(int,raw_input().split())
rArray=array[::-1]
for turns in range(d):
    p=rArray.pop()
    array.append(p)
    array.remove(p)
for elements in array:
    print elements,    
