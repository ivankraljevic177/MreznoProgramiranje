import socket

host = socket.gethostname()
port = 12345
IPAddr = socket.gethostbyname(host)  

echo_server = socket.socket()
echo_server.bind((host,port))
echo_server.listen(5)

print (IPAddr)


print ("Cekam klijenta...")
conn, addr = echo_server.accept()

print ("Spojen: ", addr)

while True:
	data = conn.recv(1024)
	if not data: break
	conn.sendall(data)
	
conn.close()