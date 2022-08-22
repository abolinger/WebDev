fname = input('Enter file name: ')
fh = open(fname)
count = 0
tot = 0
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        pos = line.find('0')
        num = float(line[pos : ])
        count = count + 1
        tot = tot + num
        avg = tot / count
print('Average spam confidence:', avg)
