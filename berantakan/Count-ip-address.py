import ipaddress

def ips_between(start, end):
    # TODO
    ip1 = ipaddress.IPv4Address(start)
    ip2 = ipaddress.IPv4Address(end)

    ip1 = int(ip1)
    ip2 = int(ip2)

    total = abs(ip1-ip2)
    
    return total

print(ips_between("20.0.0.10", "20.0.1.0"))
