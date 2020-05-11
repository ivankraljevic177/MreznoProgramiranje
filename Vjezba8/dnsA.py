import dns.resolver

result = dns.resolver.query('tutorialspoint.com', 'A')
for ipval in result:
    print('IP', ipval.to_text())