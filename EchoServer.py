import sys
from thread import *
from socket import *

HOST = ""
DEFAULT_PORT = 54320

class EchoServer(object):
    
    def __init__(self, port = DEFAULT_PORT):
        self.sock = socket()
        self.port = port
        self.isrunning = False
        try:
            self.sock.bind((HOST, port))
        except IOError, msg:
            print "Bind failed: " + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()
        self.sock.settimeout(30)
    
    def getPort(self):
        return self.port
    
    def _handleclient(self, conn):
        conn.send("Hi, type smth\n")
        conn.settimeout(None)
        client_is_sending = True
        while client_is_sending:
            try:
                data = conn.recv(1024)
                
                conn.send(data)
            except IOError , msg:
                print msg
                client_is_sending = False
        conn.close()
    
    def start(self):
        self.sock.listen(5)
        print "Start listening"
        self.isrunning = True
        
        while self.isrunning:
            try:
                conn, addr= self.sock.accept()
                print "Connection: " + str(addr)
                
                start_new_thread(self._handleclient, (conn,))
            except IOError , msg:
                print msg
                self.isrunning = False
    
    def stop(self):
        self.sock.close()
        print "Connection closed"
    
    def isRunning(self):
        return self.isrunning
