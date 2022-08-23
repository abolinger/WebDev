import re
fname = '<your file here>'
fhandle = open(fname)
x = fhandle.read()
y = re.findall('[0-9]+', x)      #this pulls all numbers out of the text file
total = 0
for num in y:
    num = int(num)
    total = total + num          #this takes the list of numbers to get the sum
print(total)
