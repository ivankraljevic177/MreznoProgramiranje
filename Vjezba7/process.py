import datetime
import socket
import sys
import multiprocessing
import datetime
import os

def port_scanner(arg):
    targetIP, PortNumber = arg
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = tcp_sock.connect_ex((targetIP,PortNumber))
    
    if result == 0:
        return PortNumber, True
        
    else: 
        return PortNumber, False
        
    tcp_sock.close()
    
    
def info():

    print ("vrijeme pokretanja ovog programa:")
    print (datetime.datetime.now())
    print ("program se izvodi na ovom racunalu:")
    
    
def pool_handler(ports):
    brojCore = multiprocessing.cpu_count()
    print ("broj core-ova ovog procesora je %d, a kreirat cemo %d procesa" % (brojCore, brojCore*2))
    pool = multiprocessing.Pool(processes=brojCore*2)
    
    for port, status in pool.map(port_scanner, [(targetIP,port) for port in ports]):
        print ("Skeniram port: %d" % (port)) 
        if status == True:
            print ("port %d je otvoren" %(port)) 
        else: 
            print ("port closed %s" %(port))


if __name__ == "__main__":
    print ("---------------------------------------------------------")
    print ("Molim vas unesite adresu hosta koju zelite testirati:")
    target =input(">> ")

    try:

        targetIP = socket.gethostbyname(target)
        print ("Skeniram host %s, IP adresu: %s" % (target, targetIP))
        print ("Unesite od kojeg do kojeg porta zelite napraviti skeniranje?")
        up = os.system('ping ' + targetIP + ' -n 1')
        if up == 0:
            start =input("Pocetni port >> ")
            end =input("Zavrsni port >> ")
            
            start_time = datetime.datetime.now()
            ports = range(int(start),int(end)+1)
            pool_handler(ports)
            elapsed_time = datetime.datetime.now() - start_time
            print ("\nSkeniranje portova zavrseno!")
            print ("Trajanje: %s "% (elapsed_time)) 
        else:
            print("." *50)
            print ("\nHost %s nije dostupan. Program zavrsava!" %host)
        
        

    except socket.gaierror:
        print ("Zapis nije u DNS-u!")
        



