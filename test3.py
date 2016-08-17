from netaddr import *

class IPv4Address(object):
    
    def __init__(self, address):
        if type(address) is str:
            self.ip = address
            self.string_ip = address.split(".")
            if len(self.string_ip) is not 4:
                raise ValueError("IllegalArgumentException")
            for octet in self.string_ip:
                if int(octet) < 0 or int(octet) > 255:
                    raise ValueError("IllegalArgumentException")
            n = 24
            self.long_ip = 0
            for octet in self.string_ip:
                self.long_ip += long(octet) << n
                n -= 8
        elif type(address) is long:
            if address < 0 or address > 4294967295:
                raise ValueError("IllegalArgumentException")
            self.long_ip = address
    
    def __lt__(self, other):
        return (isinstance(other, IPv4Address)) and self.ip < other.ip
    
    def __gt__(self, other):
        return (isinstance(other, IPv4Address)) and self.ip > other.ip
    
    def __eq__(self, other):
        return (isinstance(other, IPv4Address)) and self.__dict__ == other.__dict__
    
    def toString(self):
        return str(self.ip)
    
    def toLong(self):
        return long(self.ip)

ip = IPv4Address("127.12.45.22")

print ip.string_ip
print ip.long_ip
