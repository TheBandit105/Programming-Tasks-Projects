import socket
import psutil

## hostname = socket.gethostname()

## print(socket.gethostbyname(hostname))

interfaces = psutil.net_if_addrs()
stats = psutil.net_if_stats()

for name, addresses in interfaces.items():
       print(name)

       if stats[name].isup:
          print('Status: Up')
       else:
          print('Status: Down') 

       for address in addresses:
          if address.family == socket.AF_INET:
               print(f'IPv4: {address.address}')
               