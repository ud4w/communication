import os


string = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
string = string.split("\r\n", 1)[0]
print string

# print lst
f = open("mime.types")

data = f.read()

udata = data.split()
i = 0
for word in udata:
    if word[-1] is ";":
        word += " "
        word += udata[i+1]
        udata[i] = word
        del udata[i+1]
    i += 1
lst = udata[0::2]
# del lst[1::2]
print lst
print udata
# i = 0
# print len(udata)
# for word in udata:
#     # if i % 2 == 0:
#     del udata[i]
#     i += 2


# data.replace("\n", "")

# print udata
# udata = ""
# print data
# for line in data:
#     word = line.replace("\n", "")
#     udata += (word.rsplit(None, 1)[-1])
#     udata += " "
#     # return_string.append()
# udata = udata[:-1]

# f.close()

# address, port, root_dir = udata.rsplit(" ", 2)

# print address == "127.0.0.1"
# print port == "80"
# print root_dir == "d:/folders/jd/communication/"
# print udata
# print data
