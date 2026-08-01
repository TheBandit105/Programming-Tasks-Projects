import socket
import os
import platform
import sys

def get_system_info():
    return {
        "Computer Name": socket.gethostname(), 
        "Username": os.getlogin(), 
        "Windows Family": os.name, 
        "Operating System (OS)": platform.system(), 
        "Windows Version": platform.version(), 
        "Platform": sys.platform, 
        "Processor": platform.processor()
    }