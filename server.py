import socket
import sys
import threading

class chatApp:
	def __init__(self):
    self.host = socket.gethostname() 
	  self.port = 12353
		self.s  = socket.socket() 
		self.s.bind((self.host,self.port)) #create socket
    self.s.listen(5) #check for client requests 
    self.c,self.addr = self.s.accept() # accept client request
		print "Got Connection from",self.addr
    #receive data from client
	def receive(self):
		while True:
			k = self.c.recv(1024)
			print "\t"+k
			continue
    #send data to client
	def send(self):
		while True:
			k = raw_input()
			self.c.send(k)
			continue
      #Threads to send and receive data
    def run(self):
        t1 = threading.Thread(target=self.send)
        t2 = threading.Thread(target=self.receive)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
		print(self.send,self.receive)

c = chatApp()
c.run()
	
