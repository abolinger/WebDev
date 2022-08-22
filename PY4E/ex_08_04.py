fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
words = list()
for line in fh:
    a = line.split()
    for word in a:
        if word not in words:
            words.append(word)
words.sort()
print(words)
