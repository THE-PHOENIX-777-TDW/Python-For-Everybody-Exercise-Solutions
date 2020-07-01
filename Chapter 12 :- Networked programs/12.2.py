import socket
store="".encode()
count=0
while True:
    try:
        url_add=input("Enter Link : ")
        cont=url_add.split("/")
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((cont[2], 80))
        string='GET '+url_add+' HTTP/1.0\r\n\r\n'
        cmd = string.encode()
        mysock.send(cmd)
        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            count+=len(data)
            store=store+data
        print(store[:200].decode(),end='')
        print("\n",count)
        mysock.close()
        break
    except:
        print("Unable to Connect")

