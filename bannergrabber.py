#!/usr/bin/python3

import socket

s = socket.socket()

ip = input("What is the IP address?: ")
port = str(input("Please Enter the Port: "))
s.connect((ip, int(port)))

print(s.recv(1024))

