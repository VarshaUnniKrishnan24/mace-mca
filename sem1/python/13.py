d1=dict(((3,'Aishwarya'),(4,'Alen'),(2,'anit'),(1,'aby')))
c={x:d1[x] for x in sorted(d1)}
print('ascending order:',c)
c={x:d1[x] for x in sorted(d1,reverse=True)}
print('descending order:',c)
