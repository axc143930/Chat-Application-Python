import socket
import sys
import threading


class chatApp:
	def __init__(self):	
		self.host = socket.gethostname()
		self.port = 12353
        	self.s = socket.socket()
        	self.flag = 0
		self.s.connect((self.host,self.port))
                 
	def send(self):
		while True:
			k = raw_input()
			print k
			self.s.send(k)
			continue
	
	def receive(self):
		while True:
			k = self.s.recv(1024)	
			print "\t"+k
			continue

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
