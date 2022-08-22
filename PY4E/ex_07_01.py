fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
inp = fhandle.read()
i = inp.strip()
print(i.upper())
