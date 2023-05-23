#!/usr/bin/python3

import socket

def banner(ip, port):
    s = socket.socket()
    s.settimeout(5)
    s.connect((ip, int(port)))
    print(str(s.recv(1024)).strip('b'))


def main():
    ip = input("Please input the IP address here: ")
    port = str(input('Please Enter The Port: '))
    banner(ip, port)

main()
