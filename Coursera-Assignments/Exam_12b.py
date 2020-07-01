import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url = input('Enter Url: ')
count=int(input("Enter count: "))
pos=int(input("Enter position: "))
for i in range(count+1):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    con=tags[pos-1]
    print("Retrieving:",url)
    url=str(con.get('href', None))
    



