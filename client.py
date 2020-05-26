import socket
import threading

print ("Hello world")
DATA_BUFFER = 8
PORT = 1234
IP_ADDRESS = "192.168.1.113"
ADDRESS = (IP_ADDRESS,PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDRESS)

def send(message):
	message = message.encode(FORMAT)
	msg_length = len(message)
	msg_length = str(msg_length).encode(FORMAT)
	msg_length += b' '*(DATA_BUFFER - len(msg_length))
	client.send(msg_length)
	client.send(message)

def receive():
	while 1:
		message = client.recv(DATA_BUFFER).decode(FORMAT)
		
		if message != 0:
			try:
				message_length = int(message)
			except:
				continue
				
			msg = client.recv(message_length).decode(FORMAT)
			print (f'\n {msg}')
		else:
			pass


thread = threading.Thread(target=receive)
thread.start()

while 1:
	msg = input()
	send(msg)
