import socket
import os
import platform
import sys

"""
System Information Collector

Collects basic operating system and device information.

The values returned here are intended for troubleshooting
purposes and are displayed within the FieldAssist report.

Future Improvements:
- Replace platform module values with Windows CIM/WMI.
- Retrieve Manufacturer.
- Retrieve Model.
- Retrieve BIOS Version.
- Retrieve Friendly CPU Name.
"""

# TODO:
# Replace platform.system() and platform.processor()
# with Windows CIM queries to better match System Information (msinfo32).

def get_system_info():

    """
    Collect basic system information.

    Returns:
        dict:
            A dictionary containing operating system
            and computer information.
    """

    return {
        "Computer Name": socket.gethostname(), 
        "Username": os.getlogin(), 
        "Windows Family": os.name, 
        "Operating System (OS)": platform.system(), 
        "Windows Version": platform.version(), 
        "Platform": sys.platform, 
        "Processor": platform.processor()
    }