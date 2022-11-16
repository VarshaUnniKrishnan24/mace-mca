s=list(input("enter the sentance:").split())
d={}
for w in s:
    d[len(w)]=d.get(len(w),0)+1
print("length of longest word:",max(d.keys()))
if(d[max(d.keys())]>1):
      print('BINGO')
