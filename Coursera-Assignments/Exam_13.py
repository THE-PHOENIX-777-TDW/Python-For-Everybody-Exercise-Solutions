import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

Total=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url=input("Enter Url: ")
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('.//count')
    for i in range(len(results)):
        lat = results[i].text
        Total+=int(lat)

    print('Total:', Total)
