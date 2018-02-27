import socket

def main():
	ip = '127.0.0.1'
	port = 5005
	buff_size = 1024
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.bind((ip, port))
	socket.listen(1)

	conn, addr = socket.accept()
	print("Connection address: ", addr)

	while 1:
		data = conn.recv(buff_size)
		if not data: break
		print("Received data: ", data)
		conn.send(data)
	conn.close()


if __name__ == '__main__':
	main()


