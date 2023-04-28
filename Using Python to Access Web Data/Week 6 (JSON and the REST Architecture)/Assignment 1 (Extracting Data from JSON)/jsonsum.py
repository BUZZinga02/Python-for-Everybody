import urllib.request, urllib.parse, urllib.error
import json

data = input('Enter URL: ')
dat=urllib.request.urlopen(data).read().decode()
info = json.loads(dat)
totalcountt=0
for item in info["comments"]:
    current_count=int(item["count"])
    totalcount+=current_count

print('Sum:',totalcount)
