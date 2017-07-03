import re
def phoneNumberVerification():
    n=input()
    pattern="^[789]"
    for i in range(n):
        number=raw_input()
        if len(number)==10 and number.isdigit():
            ans=re.findall(pattern,number)
            if len(ans)==1:
                print "YES"
            else:
                print "NO"    
        else:
            print "NO"            


phoneNumberVerification()             