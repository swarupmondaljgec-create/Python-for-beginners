import urllib.request
import json
response = urllib.request.urlopen('https://uselessfacts.jsph.pl//api/v2/facts/random')
print(response.getcode())
data = response.read()
# print(data)
thejson=json.loads(data)
print(thejson["text"])