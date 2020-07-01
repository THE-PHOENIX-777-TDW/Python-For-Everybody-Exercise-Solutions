import socket

while True:
    try:
        url_add=input("Enter Link : ")
        cont=url_add.split("/")
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((cont[2], 80))
        st='GET '+url_add+' HTTP/1.0\r\n\r\n'
        cmd = st.encode()
        mysock.send(cmd)

        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            print(data.decode(),end='')
    
        mysock.close()
        break
    except:
        print("Unable to Connect")
