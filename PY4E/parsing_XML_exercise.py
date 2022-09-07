import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter link: ')

print('Retrieving', address)
uh = urllib.request.urlopen(address, context = ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
total = 0
tree = ET.fromstring(data)
for count in tree.iter('count'):
    new_count = int(count.text)
    total = total + new_count
print('Sum:', total)
