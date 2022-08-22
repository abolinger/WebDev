fname = input('Enter file: ')
try:
    fhandle = open(fname)
except:
    print('File could not be opened:', fname)
    quit()
times = dict()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1:
        continue
    if words[0] != 'From':
        continue
    time = words[5]
    timestamp = time.split(':')
    times[timestamp[0]] = times.get(timestamp[0],0) + 1
x = sorted(times.items())
for k,v in x:
    print(k,v)
