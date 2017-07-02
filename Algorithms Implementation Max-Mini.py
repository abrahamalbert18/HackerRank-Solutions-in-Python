a,b,c,d,e = raw_input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
numbers=[a,b,c,d,e]
total=sum(numbers)
maximum=total-min(numbers)
minimum=total-max(numbers)
print maximum
print minimum

