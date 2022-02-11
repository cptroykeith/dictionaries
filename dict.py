'''
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 27
purse['perform'] = 21
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 4
print(purse)
'''
#counting with a dictionary
'''
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)
'''
'''
counts = dict()
names = ['cwen', 'csev', 'zqian', 'csev', 'cwen']
for name in names :
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)
#count with get()
counts = dict()
names = ['cwen', 'csev', 'zqian', 'csev', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)
'''
#loops
counts = dict()
line = input('Enter a line of text:')
words = line.split()

print('words:', words)
print('counting...')

for word in words: 
    counts[words] =counts.get(word,0) + 1
print('counts', counts)

