t = int(raw_input().strip())
def costOfBlackGifts(x,y,z):
    if y+z < x:
        return y+z
    else:
        return x
    
def costOfWhiteGifts(x,y,z):
    if x+z < y:
        return x+z
    else:
        return y
    
for a0 in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [long(b),long(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [long(x),long(y),long(z)]
    cost=b*costOfBlackGifts(x,y,z) + w* costOfWhiteGifts(x,y,z)
    print cost
        
        

