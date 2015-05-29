#!/usr/bin/python
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 5000))
while True:
	s.listen(1)
	conn, addr = s.accept()
	conn.sendall(addr[0])
