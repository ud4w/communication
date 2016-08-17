from IPv4Address import *

class Network(object):
    
    def __init__(self, address, maskLenght):
        self.net = IPNetwork(address.ip)
        self.net.prefixlen = maskLenght
    
    def toString(self):
        return str(self.net)
    
    def getAddress(self):
        return self.net.ip
    
    def getBroadcastAddress(self):
        return self.net.broadcast
    
    def contains(self, address):
        return self.net.__contains__(address.ip)
    
    def getFirstUsableAddress(self):
        return list(self.net) [1]
    
    def getLastUsableAddress(self):
        return list(self.net) [-2]
    
    def getMask(self):
        return long(self.net.netmask)
    
    def getMaskString(self):
        return str(self.net.netmask)
    
    def getMaskLenght(self):
        return self.net.prefixlen
    
    def getSubnets(self):
        subnets = list(self.net.subnet(self.getMaskLenght() + 1))
        print subnets
        address1 = IPv4Address(subnets[0].ip)
        address2 = IPv4Address(subnets[1].ip)
        Network_list = [Network(address1, subnets[0].prefixlen), Network(address2, subnets[1].prefixlen)]
        return Network_list
    
    def isPublic(self):
        return not self.net.is_private()
    
    def getTotalHosts(self):
        return self.net.size - 2
