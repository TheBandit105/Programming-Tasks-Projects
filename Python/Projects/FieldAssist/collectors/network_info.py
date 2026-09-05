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

         # Ignore MAC and IPv6 entries for the current prototype.
         if address.family == socket.AF_INET:

            # Convert the boolean interface state into a readable status.
            status = "Up" if stats[name].isup else "Down"
            
            network_info.append({
                  "Name": name, 
                  "Status": status, 
                  "IPv4": address.address
                  })
         


   return network_info

   
               #"Name": f"{name}"
              # "Status": f"Up"
               #"IPv4": f"{address.address}"
        
            
              # "Name": f"{name}"
              # "Status": f"Down"
               #"IPv4": f"{address.address}"