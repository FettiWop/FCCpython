#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = "your local ip'
host = socket.gethostbyname()
#the port to connect to.
port = 444
#binding address port to socket.
serversocket.bind(('172.20.20.127', port))

#tcp listener connections, here we can change the number of connections we can make to this server.
serversocket.listen(3)
while True:
    clientsocket, address = serversocket.accept()

    print("received connection from %s " % str(address))

    message = 'Thank you for connecting to the fetti server' + "\r\n"
    clientsocket.send(message('ascii'))

    clientsocket.close()

