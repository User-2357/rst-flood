from socket import *

s = socket(AF_PACKET, SOCK_RAW, 0x8100)
s.bind(('eth0', 0x8100))

res=''
for i in packet.split(' '):
    res += chr(int(i, 16))
s.send(res)
