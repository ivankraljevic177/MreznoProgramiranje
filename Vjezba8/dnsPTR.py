import dns.resolver 

myDnsResolver = dns.resolver.Resolver() 
result = myDnsResolver.query("3.125.194.174.in-addr.arpa", "PTR") 
for data in result: 
    print (data)