import sys
import time
from thread import *
from socket import *

class HttpServer(object):
    
    def __init__(self):
        self.config = self.file_parser("http.conf")
        self.mime_types = self.file_parser("mime.types")
        self.sock = socket()
        for i, cnf in enumerate(self.config):
            if cnf == "address":
                self.host = self.config[i+1]
            if cnf == "port":
                self.port = int(self.config[i+1])
            if cnf == "root_dir":
                self.root_dir = self.config[i+1]
        self.isrunning = False
        try:
            self.sock.bind((self.host, self.port))
        except IOError, msg:
            print "Bind failed: " + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()
    
    def _handleclient(self, conn):
        conn.send("Hi, type smth\n")
        
        request = conn.recv(1024)
        if request.split(' ', 1)[0] == "GET":
                self.get_request_handler(conn, request)
        else:
            self.send_answer(conn, status="405 Method Not Allowed", content_type="NONE")
    
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
    
    def getPort(self):
        return self.port
    
    def get_request_handler(self, conn, request):
        request = request.split("\r\n", 1)[0]
        method, path, protocol = request.split(" ", 2)
        type_list = self.mime_types[0::2]
        req_file = ""
        content_type = "application/octet-stream"
        data = ""
        
        if path == "/":
            req_file = "index.html"
            f = open(req_file)
            data = f.read()
            f.close()
            self.send_answer(conn, protocol, data=data)
            return
        else: 
            path = path.lstrip("/")
            req_file = path
        
        try:
            f = open(req_file)
            data = f.read()
            f.close()
            for i, end in enumerate(self.mime_types):
                if path.endswith(end):
                    content_type = self.mime_types[i+1]
            self.send_answer(conn, protocol, content_type, data=data)
            return
        except IOError , msg:
            self.send_answer(conn, protocol, status="404 Not Found", content_type="NONE")
            return
    
    def send_answer(self, conn, protocol="HTTP/1.1", content_type="text/html; charset=UTF-8", data="", status="200 OK"):
        print (status.split(' ', 1)[0]) + " / " + content_type
        conn.send(protocol + " " + status + "\r\n")
        conn.send("Connection: close" + "\r\n")
        conn.send("Content-Length: " + bytes(len(data)) + "\r\n")
        conn.send("Content-Type: " + content_type + "\r\n")
        conn.send("Date: " + time.strftime("%H:%M:%S %d.%m.%Y") + "\r\n")
        conn.send("\r\n")
        conn.send(data)
        
        conn.close()
    
    def file_parser(self, file_name):
        f = open(file_name)
        data = f.read()
        f.close()
        udata = data.split()
        
        i = 0
        for word in udata:
            if word[-1] is ";":
                word += " "
                word += udata[i+1]
                udata[i] = word
                del udata[i+1]
            i += 1
        
        return udata
    
    def stop(self):
        self.sock.close()
        print "Connection closed"
    
    def isRunning(self):
        return self.isrunning
