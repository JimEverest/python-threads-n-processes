from socket import *
import time

s = socket(AF_INET,SOCK_STREAM)
s.connect(('localhost',8081))
tm = s.recv(1024)
s.close()
print('The time is %s' % tm.decode('ascii'))

