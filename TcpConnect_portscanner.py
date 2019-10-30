try:
	import os
	import sys
	from scapy.all import *
	import random
except ImportError as ie:
	print(ie)



try:
	host = input(">> [?] Enter Target Host: ")
	min_port = input(">> [?] Enter Min Port: ")
	max_port = input(">> [?] Enter Max Port: ")
	ports = range(int(min_port), int(max_port)+1)
	RST = 0x14
	SYN_ACK = 0x12
	src_port = random.randint(1, 65535)
	print(">> [*]  Initiating A Full Tcp Connect Port Scan")
	print(">> [*] " + "*"*66)
	try:
		for port in ports:
			conf.verb = 0
			TCPCONNECTpkt = (IP(dst=host)/TCP(sport=src_port, dport=port, flags="S"))
			TCPCONNECTconnection = sr1(TCPCONNECTpkt, timeout=5)
			if(TCPCONNECTconnection == None):
				pass
			elif(TCPCONNECTconnection.haslayer(TCP)):
				if(TCPCONNECTconnection.getlayer(TCP).flags == SYN_ACK):
					RSTACKpkt = (IP(dst=host)/TCP(sport=src_port,dport=port,flags="RA"))
					RSTACKsend = send(RSTACKpkt)
					print(">> [+] Port " + str(port) + ": " + " OPEN")
					print(">> [*] " + "="*66)
			elif(TCPCONNECTconnection.getlayer(TCP).flags == RST):
				pass
	except Exception as e:
		print(e)
		sys.exit()
except KeyboardInterrupt as ki:
	print(">> [!] Exiting")
	sys.exit()
