import socket
import psutil
import subprocess
import json

## hostname = socket.gethostname()

## print(socket.gethostbyname(hostname))

def get_default_network():
   command = """
   $config = Get-NetIPConfiguration | Where-Object {
    $_.IPv4DefaultGateway -ne $null -and
    $_.NetAdapter.Status -eq "Up"
}

[PSCustomObject]@{
    Name = $config.InterfaceAlias
    IPv4 = $config.IPv4Address.IPAddress
    Gateway = $config.IPv4DefaultGateway.NextHop
    DNS = ($config.DNSServer | Where-Object AddressFamily -eq 2).ServerAddresses
} | ConvertTo-Json
   """

   result = subprocess.run(
         ["powershell", "-Command", command],
         capture_output=True,
         text=True)

   data = json.loads(result.stdout)
   return data


def get_network_info():
   interfaces = psutil.net_if_addrs()
   stats = psutil.net_if_stats()

   network_info = []

   for name, addresses in interfaces.items():

     ipv4 = None
     mac = None

     for address in addresses:

         # Collect IPv4 and MAC addresses; ignore IPv6 for the current prototype.
         if address.family == socket.AF_INET:
            ipv4 = address.address

         if address.family == psutil.AF_LINK:
            mac = address.address

     # Convert the boolean interface state into a readable status.
     status = "Up" if stats[name].isup else "Down"

     network_info.append({
            "Name": name, 
            "Status": status, 
            "IPv4": ipv4,
            "MAC": mac
            })
         
   return network_info

   
if __name__ == "__main__":
   print(get_default_network())
   
               #"Name": f"{name}"
              # "Status": f"Up"
               #"IPv4": f"{address.address}"
        
            
              # "Name": f"{name}"
              # "Status": f"Down"
               #"IPv4": f"{address.address}"