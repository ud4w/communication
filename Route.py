from IPv4Address import *
from Network import *

class Route(object):
    
    def __init__(self, network, gateway, interfaceName, metric):
        self.net = network
        self.gateway = IPv4Address(gateway)
        self.interface = interfaceName
        self.metric = metric
    
    def getGateway(self):
        return self.gateway
    
    def getInterfaceName(self):
        return self.interface
    
    def getMetric(self):
        return self.metric
    
    def getNetwork(self):
        return self.net
    
    def toString(self):
        if self.gateway.ip is None:
            return "net: " + self.net.toString() + ", interface: " + str(self.interface) + ", metric: " + str(self.metric)
        return "net: " + self.net.toString() + ", gateway: " + self.gateway.toString() + ", interface: " + str(self.interface) + ", metric: " + str(self.metric)
