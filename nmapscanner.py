#!/usr/bin/python3

import nmap


scanner = nmap.PortScanner()

print("Welcome to the Python nmap Scanner by FettiWop")
print("------------------------------------------------")

ip_addr = input("Please Enter The IP Address you'd like to scan!")
print("The IP Address you Enetered is: " ,ip_addr)
type(ip_addr)


resp = input("""\nPlease Enter the Type of Scan you Want to Run
                    1)SYN ACK Scan
                    2)UDP Scan
                    3)Comprehensive Scan\n""")
print("You have selected option: " ,resp)


if resp == '1':
    print("Nmap Version: " ,scanner.nmap_version)
    scanner.scan(ip-addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all-protocols)
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '2':
    print("Nmap Version: " ,scanner.nmap_version)
    scanner.scan(ip-addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all-protocols)
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())

elif resp == '3':
    print("Nmap Version: " ,scanner.nmap_version)
    scanner.scan(ip-addr, '1-64000', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all-protocols)
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

elif resp >= '4':
    print("Please Enter a Valid option")
