import dns.resolver 

myDnsResolver = dns.resolver.Resolver() 
result = myDnsResolver.query("google.com", "MX") 
for data in result: 
    print (data)