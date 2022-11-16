names=input('enter a list of names:')
count=[name for name in names.split() if name.lower().startswith('a')]
print(count)
