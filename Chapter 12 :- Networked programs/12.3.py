import urllib.request,urllib.parse, urllib.error
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

while True:
    try:
        url_add=input("Enter Link : ")
        fhand = urllib.request.urlopen(url_add).read()
        count=len(fhand)
        print(count)
        file=fhand[:3000]
        break
    except:
        print("Unable to Connect")

print(file.decode())
