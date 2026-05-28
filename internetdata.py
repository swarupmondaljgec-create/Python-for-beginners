import urllib.request
response = urllib.request.urlopen('https://www.example.com')
print(response.getcode())
data = response.read()
print(data)