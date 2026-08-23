import socket
import psutil

## hostname = socket.gethostname()

## print(socket.gethostbyname(hostname))

interfaces = psutil.net_if_addrs()

for name, addresses in interfaces.items():
	print(name)
      
	for address in addresses:
            if address.family == socket.AF_INET:
                 print(f'IPv4: {address.address}')