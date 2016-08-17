from netaddr import *

class IPv4Address(object):
    
    def __init__(self, address):
        if address != None:
            self.ip = IPAddress(address)
        else:
            self.ip = None
    
    def __lt__(self, other):
        return (isinstance(other, self.__class__)) and self.ip < other.ip
    
    def __gt__(self, other):
        return (isinstance(other, self.__class__)) and self.ip > other.ip
    
    def __eq__(self, other):
        return (isinstance(other, self.__class__)) and self.__dict__ == other.__dict__
    
    def toString(self):
        return str(self.ip)
    
    def toLong(self):
        return long(self.ip)
