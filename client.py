import socket
import sys
import threading


class chatApp:
	def __init__(self):	
		self.host = socket.gethostname()
		self.port = 12353
        	self.s = socket.socket() # create socket
        	self.flag = 0
		self.s.connect((self.host,self.port)) # connect to IP address
        # send data to server         
	def send(self):
		while True:
			k = raw_input()
			print k
			self.s.send(k)
			continue
	# receive data from server
	def receive(self):
		while True:
			k = self.s.recv(1024)	
			print "\t"+k
			continue
	# create threads to send and receive data
    	def run(self):
        	t1 = threading.Thread(target=self.send)
       		t2 = threading.Thread(target=self.receive)
        	t2.start()
        	t1.start()
        	t1.join()
        	t2.join()
		self.s.close()
		print(self.send,self.receive)

c = chatApp()
c.run()
