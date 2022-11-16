l=input("enter a string:")
count=[word for word in l.split() if word.isalpha()]
print(len(count))
