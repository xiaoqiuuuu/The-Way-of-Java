import socket
sock = socket.socket()
sock.bind(("127.0.0.1",8888))
sock.listen(5)
while 1:
    conn,addr = sock.accept()
    data = conn.recv(1024)
    print("has data:",data.decode())
    with open("index.html") as f:
        html = f.read()
    conn.send(("HTTP/1.1 200 ok\r\nContent_Length:11\r\n\r\n"+html).encode())
    conn.close()