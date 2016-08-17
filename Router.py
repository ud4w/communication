from Route import *

class Router(object):
    
    def __init__(self, routes):
        self.routes = routes
    
    def addRoute(self, route):
        if isinstance(route, Route.__class__):
            routes.append(route)
        else:
            raise ValueError('not instance of Route passed!')
    
    def getRouteForAddress(self, address):
        if isinstance(address, IPv4Address):
            mask = 0
            for route in self.routes:
                if route.getNetwork().contains(address) and route.getNetwork().getMaskLenght() >= mask:
                    mask = route.getNetwork().getMaskLenght()
                    result = route
            return result
        
        def getRoutes(self):
            return self.routes
        
        def removeRoute(self, route):
            self.routes.remove(route)
