#libraries
import os
#functions
def cmd(c):
	return os.popen(c).read()
def clear(cmd):
	os.system("clear")
	print(cmd)
def main():
	ip = input("Enter IP or Host (WITHOUT http , https , ftp , ...) :")
	min = int(input("Enter MIN port(int):"))
	max = int(input("Enter MAX port(int):"))

	num = min
	ports = []
	while num >= min and num <= max:
		conf = cmd("ping -c 2 -t "+str(num)+" "+str(ip))
		print(str(conf).replace('/n','').replace('\r',''))
		if "live" in str(conf):
			clear(f"Port {num} is Closed.")
		elif str(conf) == "" or str(conf) == None:
			clear(f"Port {num} is Closed.")
		else:
			print(f"Port {num} Is Open.")
			print(f"|||||||||||||||||||||| {conf} ||||||||||||||||||||")
			ports.append(num)
		num = num +1
	clear(f"Ports Open On {ip} =>")
	print(ports)
	input("Press Enter To Scan Again...")
	main()
main()
