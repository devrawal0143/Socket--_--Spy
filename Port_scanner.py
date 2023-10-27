import socket # library for server and client communication
from IPy import IP #class and tools for handling of IPv4 and IPv6 addresses and networks

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + ' [-_- Scanning target] ' + str(target) )
    for port in range(1,100): # for Multiple port scanning
        scan_port(converted_ip, port) 
    
def check_ip(ip): # it will check if input is ip or domain name and convert it 
    try:
        IP(ip) # if ip return ip
        return(ip)
    except ValueError: #if domain name convert it to ip
        return socket.gethostbyname(ip)

def get_banner(s): # for grabing the services using sock
    return s.recv(1024)
        
def scan_port(ipaddress, port): # Defining a function
    try: #if
        sock = socket.socket() # used to send message accross network
        sock.settimeout(0.5) # for faster port scanning
        sock.connect((ipaddress, port)) # to connect to the target
        try: # if services grabbed then print this
            banner = get_banner(sock) 
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')) ) # str(port) will hold the port number
        except:# else print this
            print('[+] Open Port ' + str(port))
    except: #else 
        pass # if port is closed it will pass
 
if __name__ == "__main__": # will only run in main program & not in lib             
    targets = input('[+] Enter Target/s to Sacn(split multiple targets with ,): ') # for taking target ipaddress  
    if ',' in targets:
        for ip_add in targets.split(','): # if ',' then split targets
            scan(ip_add.strip(' '))
    else: #else scan only 1 target
        scan(targets)
 

