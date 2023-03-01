import socket #to communicate with other machines with TCP and UDP
import termcolor #print statements in different colors


def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports): #runs the scan_port function for every port
		scan_port(target,port)

def scan_port(ipaddress, port): #function takes in IP address of target computer and its target port
	try:
		sock = socket.socket() #when making connection over TCP / UDP, must initiate a socket object using socket function from socket library
		sock.connect((ipaddress, port)) #connect to target and its port
		print("[+] Port Opened " + str(port)) #upon successful connection, state number of open port
		sock.close() #close the socket object
	except: #for failed connection
		pass

targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets: #if user specified multiple targets
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','): #prepare and iterate through a collection of IP addresses
		scan(ip_addr.strip(' '), ports)
else: #user specifies one target
	scan(targets,ports)
