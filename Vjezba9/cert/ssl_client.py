import socket, ssl, datetime

print ("Program started at this time: ")
print (datetime.datetime.now())

t1 =datetime.datetime.now()

print (t1)
client_socket = socket.socket()
host = "localhost"
port=10001

print(host)

ssl_client_socket = ssl.wrap_socket(client_socket, ca_certs="cert.pem", cert_reqs = ssl.CERT_REQUIRED)

ssl_client_socket.connect((host,port))


print (ssl_client_socket.recv(1024))

ssl_client_socket.close()
t2 =datetime.datetime.now()

total = t2-t1
print ("Scanning took %s min " %(total))