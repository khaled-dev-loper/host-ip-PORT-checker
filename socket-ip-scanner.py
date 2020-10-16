#Librareis
from socket import *
ip = input('Enter your ip: ')
port = []
num = 1
while num > 0 and num <65536:
	print(f'port {num} added.')
	port.append(num)
	num= num+1
print("Port Added in list")
worked_ports = []
try:
	for p in port:
		so = socket(AF_INET,SOCK_STREAM)
		so.settimeout(1)
		out = so.connect_ex((ip,p))
		if out==0:
			print(f'port {p} is open')
			worked_ports.append(p)
		else:
			print(f'port {p} is not working')
except KeyboardInterrupt:
	print("Scan Stopped because You Pressed Ctrl + C ")
finally:
	print("This Is Open Ports =>")
	print(worked_ports)
