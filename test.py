
ip = "127.12.45.22"

print ip.split(".")
string_ip = ip.split(".")
print len(string_ip)
print type(ip) is str
octet_1 = int(string_ip[0])
octet_2 = int(string_ip[1])
octet_3 = int(string_ip[2])
octet_4 = int(string_ip[3])

octets = [octet_1, octet_2, octet_3, octet_4]

long_ip = 0
n = 24
for octet in string_ip:
    long_ip += long(octet) << n
    n -= 8

# long_ip += octet_1 << 24
# long_ip += octet_2 << 16
# long_ip += octet_3 << 8
# long_ip += octet_4


print oct(long_ip)

# from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# import os

# class HttpReqHandler(BaseHTTPRequestHandler):
    
#     def do_GET(self):
#         directory = "d:/folders/JD/communication/"
        
#         try:
#             if self.path.endswith('.html'):
#                 print self.path
#                 my_file = open(directory + self.path)
                
#                 self.send_response(200)
                
#                 self.send_header('Content-type', 'text-html')
#                 self.end_headers()
                
#                 self.wfile.write(my_file.read())
#                 my_file.close()
#                 return
#         except IOError , msg:
#             print msg
#             self.send_error(404, 'file not found')
    
# def run():
#     print "http server is going to run"
    
#     server_addres = ('127.0.0.1', 80)
#     http_server = HTTPServer(server_addres, HttpReqHandler)
#     print "http server IS running "
#     http_server.serve_forever()
