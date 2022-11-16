 
n=input("enter a list of numbers:")
n=list(map(int,n.split()))
count=[num for num in n if num>0]
print(count)

n=input("enter a list of numbers:")
n=list(map(int,n.split()))
c=[num**2 for num in n]
print(c)

word=input("enter a word:")
p=[c for c in word if c.lower() in 'aeiou']
print(p)

w=input("enter the word")
p=[ord(x) for x in w]
print(p)

n=input("enter a list of numbers:")
n=list(map(int,n.split()))
p=[num for num in n if num%2]
print(p)

n=input("enter final year:")
p=[year for year in range(2022,int(n))if(year%400==0)or(year%100 and year%4==0)]
print(p)
