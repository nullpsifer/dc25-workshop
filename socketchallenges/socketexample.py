import socket

def socketexample(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    f = sock.makefile()
    print(f.readline())
    sock.send('test')
    f.close()
    sock.close()
