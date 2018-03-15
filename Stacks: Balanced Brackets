def is_matched(expression):
    s = []
    for e in expression: 
        if (e == '{'):
            s.append('}')
        elif (e == '['):
            s.append(']')
        elif (e == '('):
            s.append(')')
        else:
            if (s == [] or e != s[-1]):
                return False
            s.pop();
    return s ==[]

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
