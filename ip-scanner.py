#libraries
import os
#functions
def cmd(c):
	return os.popen(c).read()
def search(s,w):
	return (' '+w+' ') in (' '+s+' ')	
#inputs
ip = input("Enter IP or Host (WITHOUT http , https , ftp , ...) :")
min = int(input("Enter MIN port(int):"))
max = int(input("Enter MAX port(int):"))

num = min
ports = []
while num >= min and num <= max:
	conf = cmd("ping -c 2 -t "+str(num)+" "+str(ip))
	print(conf)
	if " " in str(conf):
		print(f"Port {num} is Closed.")
	else:
		print(f"Port {num} Is Open.")
		ports.append(num)
	num = num +1
print(num)
print("Application Ended")
