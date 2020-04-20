import datetime
import socket
import threading
from queue import Queue


def scanPort(port):
    s1 = socket.socket()
    result = s1.connect_ex((targetIP, port))
    if result == 0:
        print ("Port %s open" %(port))
    else: 
        print ("port closed %s" %(port))
    s1.close()
    
def worker():
    while True:
        item = q.get()
        if item is None:
            break
        scanPort(item)
        q.task_done()
        
 

print ("Vrijeme pokretanja ovog programa:")
print (datetime.datetime.now())
print ("Program se izvodi na ovom racunalu:")



print ("---------------------------------------------------------")
print ("Molim vas unesite adresu hosta koju zelite testirati:")
target =input(">> ")
q = Queue()
print_lock = threading.Lock()


try:

        targetIP = socket.gethostbyname(target)
        print ("Skeniram host %s, IP adresu: %s" % (target, targetIP))
        print ("Unesite od kojeg do kojeg porta zelite napraviti skeniranje?")
        start =input("Pocetni port >> ")
        end =input("Zavrsni port >> ")
        start_time = datetime.datetime.now()
        for t in range (10):
                t=threading.Thread(target=worker)
                t.daemon = True
                t.start()
                
        for port in range(int(start),int(end)+1):
                q.put(port)
                
        q.join()
        elapsed_time = datetime.datetime.now() - start_time
        
        print ("\nSkeniranje portova zavrseno!")
        print ("Trajanje: %s "% (elapsed_time)) 

except socket.gaierror:
        print ("Zapis nije u DNS-u!")