import socket
from datetime import datetime
from struct import *

size=500

f=open('./sao_1.jpg', 'rb') 
data = f.read()
f.close()

start=0
end=start+int(len(data)/size)+1
all_data=len(data)
m=pack('L',all_data)
n=pack('H',size)
i=unpack('L',m)
j=unpack('H',n)

print(len(data))
print(m)
print(n)
print(i[0])
print(j[0])