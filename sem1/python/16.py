count={}
word=input("enter a word:")
for w in word.lower():
 count[w]=count.get(w,0)+1
print(count)
