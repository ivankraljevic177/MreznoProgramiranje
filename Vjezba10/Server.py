import socket 
from _thread import *
import threading
import datetime

print("Vrijeme pokretanja ovog programa:")
t1 = datetime.datetime.now()
print(t1)
print("----------------------------------------------")

print_lock= threading.Lock()

def threaded(c):
    while True:
        data=c.recv(1024)
        if not data:
            print('Bye')
            
            print_lock.release()
            break
        data=data[::-1]
        c.send(data)
        
    c.close()
def Main():
    host=""
    
    port=9999
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    print("socket behind to port",port)
    
    s.listen(5)
    print("socket is listening")
    
    while True:
        c,addr=s.accept()
        
        print_lock.acquire()
        print('Connected to : ' , addr[0], ':' , addr[1])
        
        start_new_thread(threaded, (c,))
    s.close()

if __name__=='__main__':
    Main()