fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 1:
        continue
    if wds[0] != 'From':
        continue
    if line.startswith('From'):
        count = count + 1
    print(wds[1])
print('There were', count, 'lines in the file with From as the first word')
