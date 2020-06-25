import socket, datetime
import sys

print ("Vrijeme pokretanja programa : ")

t1 =datetime.datetime.now()

print (t1)
host = socket.gethostname()
port=9999

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))
print("Unesite svoje ime i prezime")
message=input()

def Main():

    while True: 
        s.send(message.encode('ascii'))
        data=s.recv(1024)
    
        print('Received from the server: ' , str(data.decode('ascii')))
    
        ans=input('Za izlazak iz programa unesite "exit":  ')
        if ans =='exit':
            print("Doviđenja")
            break
        else:
            continue
    s.close()

if message =='Ivan Kraljević':
    Main()
else:
    print("Pogrešan unos")
    sys.exit()