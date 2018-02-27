from __future__ import print_function
from socket import *
import sys, socket, select
from sys import argv

def sendChat(message):
	ip = '127.0.0.1'
	port = 5005
	buff_size = 1024
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	myMessage = message
	socket.connect((ip, port))
	socket.send(myMessage)
	data = socket.recv(buff_size)
	socket.close()
	print("Received data: ", data)


def main():
	message = input("Enter the message you wish to send: ")
	sendChat(message)

if __name__ == '__main__' :
	main()
