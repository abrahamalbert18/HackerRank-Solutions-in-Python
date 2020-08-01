def checkPalindrome(string):
    """
    Simple and clean way to write.
    This code expects phrase with no punctuations, however you can write additional code to 
    remove punctuations by using string methods. 
    """
    string = string.replace(" ", "").lower() #you can strip additional punctuations here
    reversedString = string[::-1]
    return string == reversedString
            
if __name__=="__main__":
  checkPalindrome(input("Please enter the phrase :"))
