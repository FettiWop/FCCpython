#!/usr/bin/python3

#This is a simple python script to scan a single port on a host.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("IP ADDRESS OF TARGET HERE: ")
port = int(input("Please enter the port you want to scan: "))

def portScanner():
    if s.connect_ex((host, port)):
        print("The Port is Closed!")
    else:
        print("The Port is Open!")

portScanner(port)
