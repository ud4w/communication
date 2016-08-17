# from IPv4Address import *
# from Network import *
# from Route import *
# from Router import *
# from EchoServer import *
# from HttpServer import *
from test3 import *

# Httpserver = HttpServer()
# Httpserver.start()
# server = EchoServer()

# print server.isRunning()
# print server.getPort()

# server.start()
# print server.isRunning()
# server.stop()
# print server.isRunning()

# ip = IPv4Address("0.0.0.0")
# ip2 = IPv4Address("192.168.0.0")
# ip3 = IPv4Address("10.0.0.0")
# ip4 = IPv4Address("10.123.0.0")

# net = Network(ip, 0)
# net2 = Network(ip2, 24)
# net3 = Network(ip3, 8)
# net4 = Network(ip4, 20)

# route = Route(net, "192.168.0.0", "en0", 10)
# route2 = Route(net2, None, "en0", 10)
# route3 = Route(net3, "10.123.0.1", "en1", 10)
# route4 = Route(net4, None, "en1", 10)

# routes = [route, route2, route3, route4]

# router = Router(routes)

# route5 = router.getRouteForAddress(IPv4Address("192.168.0.176"))
# print route5.getMetric()
# print route5.getInterfaceName()

# net5 = route5.getNetwork()
# print net5.toString()
# print net5.getAddress()

# route5 = router.getRouteForAddress(IPv4Address("10.0.1.1"))

# print route5.getMetric()
# print route5.getInterfaceName()

# net5 = route5.getNetwork()
# print net5.toString()
# print net5.getAddress()

# print route5.toString()

# # print net.toString()
# # print net.getAddress()
# # print net.getBroadcastAddress()
# print net.contains(ip)
# print net.getFirstUsableAddress()
# print net.getLastUsableAddress()
# print net.getMask()
# print net.getMaskString()
# print net.getMaskLenght()

# # print net.getSubnets()
# print net.isPublic()

# subnets = net.getSubnets()

# print subnets[0].toString()
# print subnets[0].getAddress()
# print subnets[0].getFirstUsableAddress()
# print subnets[0].getLastUsableAddress()
# print subnets[0].getMaskLenght()

# print net.getTotalHosts()


# print net.getSubnets()[0].getMaskLenght()
# print ip < ip2
#print ip2 == ip3
# print ip2 < ip


# print ip.toString()
# print ip.toLong()
