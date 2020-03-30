import socket 

host = socket.gethostname()
port = 12345
client_socket = socket.socket()

client_socket.connect((host, port))

client_socket.sendall('tekst koji se salje serveru')

data = client_socket.recv(1024)

print (data)
client_socket.close()

print (datetime.datetime.now())