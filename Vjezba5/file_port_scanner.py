import datetime
import socket


print ("Program started at this time: ")
print (datetime.datetime.now())

t1 =datetime.datetime.now()

print (t1)
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr) 


print ("Enter host address for testing")
target =input(">> ")
targetIP = socket.gethostbyname(target)
print ("Scanning host %s, IP address: %s" % (target, targetIP))
print ("Enter start and end port for testing")
start =input(" Enter start port: ")
end =input(" Enter end port: ")

print ("Scanning host: %s, IP address: %s" % (target, targetIP))

try:
    for port in range(int(start),int(end)):
        s1 = socket.socket()
        result = s1.connect_ex((targetIP, port))
        if result == 0:
            print ("Port %s open" %(port))
        else:
            print ("port closed %s" %(port))
        s1.close()




except KeyboardInterrupt:
    print ("Exit")
    sys.exit()

except socket.gaierror:
    print ("Hostname does not exist")
    sys.exit()

except socket.error:
    print ("Cant connect to server")
    sys.exit()




print ("Scanning done!")
t2 =datetime.datetime.now()

total = t2-t1;
print ("Scanning took %s min " %(total));
