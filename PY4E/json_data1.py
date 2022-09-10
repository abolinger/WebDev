import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter link: ')

parms = dict()
parms['address'] = address
url = address + urllib.parse.urlencode(parms)
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

comments = js.get("comments")

total = 0
for item in comments:
    vals = list(item.values())
    total += vals[1]
print('Sum:', total)
