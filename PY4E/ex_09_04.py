fname = input('Enter file: ')
try:
    fh = open(fname)
except:
    print('File could not be opened:', fname)
    quit()
counts = dict()
for line in fh:
    words = line.split()
    if len(words) < 1:
        continue
    if words[0] != 'From':
        continue
    counts[words[1]] = counts.get(words[1],0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
