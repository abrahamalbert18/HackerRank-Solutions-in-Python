h = map(int,raw_input().strip().split(' '))
word = raw_input().strip()
width= 1*len(word)
wordHeights=[]
for w in word:
    wordHeights.append(h[ord(w)-97])
height= max(wordHeights)
print height * width
