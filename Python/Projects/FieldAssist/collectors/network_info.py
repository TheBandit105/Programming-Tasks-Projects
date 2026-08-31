import socket
import psutil

## hostname = socket.gethostname()

## print(socket.gethostbyname(hostname))

def get_network_info():
   interfaces = psutil.net_if_addrs()
   stats = psutil.net_if_stats()

   network_info = []

   for name, addresses in interfaces.items():
      for address in addresses:
         if stats[name].isup or address.family == socket.AF_INET:
            network_info.append([name, "Up", address.address])
         else:
            network_info.append([name, "Down", address.address])


   return network_info

   
               #"Name": f"{name}"
              # "Status": f"Up"
               #"IPv4": f"{address.address}"
        
            
              # "Name": f"{name}"
              # "Status": f"Down"
               #"IPv4": f"{address.address}"