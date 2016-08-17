from socket import *

HOST = "localhost"
DEFAULT_PORT = 54320

class WazzupClient(object):
    
    def __init__(self, port = DEFAULT_PORT):
        self.client = socket()
        self.port = port
        self.isrunning = False
        self.client.settimeout(5)
    
    def start(self):
        self.client.connect((HOST, self.port))
        self.isrunning = True
        self.client.sendall("Wazzup")
        while self.isrunning:
            try:
                # self.client.sendall("Wazzup")
                data = self.client.recv(1024)
                print data
            except IOError , msg:
                print msg
                self.isrunning = False
        
    def stop(self):
        self.client.close()
