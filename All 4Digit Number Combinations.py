#ALL the combinations of 4 digit combo
def FourDigitCombinations():
    
    for code in range(10000):
        if code<=9:
            print "000"+str(code),
        elif code>=10 and code<=99:
            print "00"+str(code),
        elif code>=100 and code<=999:
            print "0"+str(code),
        else:
            print code,
            
        
                
