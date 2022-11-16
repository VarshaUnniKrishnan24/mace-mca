words={}
line=input("enter a sentence:")
for w in line.lower().split():
 words[w]=words.get(w,0)+1
print(words)
