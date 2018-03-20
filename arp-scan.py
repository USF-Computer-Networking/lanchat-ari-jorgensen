
import socket
import subprocess
import sys


class Device:
    def __init__(self, name, ipaddr, mac, interface):
        self.name = name
        self.ipaddr = ipaddr
        self.mac = mac
        self.interface = interface

    def __repr__(self):
        return "Device({},{},{},{})".format(self.name, self.ipaddr, self.mac, self.interface)

    def __str__(self):
        return self.ipaddr


    def __str__(self):
        return "Device name: {}\nIP address: {}\nMAC address: {}\nInterface: {}\n".format(self.name, self.ipaddr, self.mac, self.interface)


def create_dev(d):
    attr = d.split(' ')
    return Device(attr[0], attr[1][1:-1], attr[3], attr[5])

def scan():
    cmd = ['arp', '-a']
    result = subprocess.check_output(cmd)
    devs = result.split('\n')
    devs.pop()
    devices = []
    for d in devs:
        devices.append(create_dev(d))
    
    for d in devices:
        print(d)

def main():
    
    print("Starting scan...\n")


    scan()
    

if __name__ == '__main__':
    main()
