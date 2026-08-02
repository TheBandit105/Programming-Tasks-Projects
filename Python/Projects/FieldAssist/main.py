from collectors.system_info import get_system_info
from collectors.disk_info import get_disk_info

"""
FieldAssist

Entry point for the FieldAssist application.

This module coordinates the different collectors and displays
their output in the terminal.

Current collectors:
- System Information
- Disk Information
"""

def main():

    """
    Run the FieldAssist diagnostic collection.

    Calls each collector module, retrieves the diagnostic
    information as dictionaries and displays the results
    in a readable format.
    """

    system = get_system_info()
    disk = get_disk_info()

    print("\n======================================================")
    print("FIELDASSIST DEVICE REPORT")
    print("======================================================\n")

    # Display the System Information section.

    print("\nSYSTEM INFORMATION")
    print("-----------------------\n")

    for key, value in system.items():
        print(f"{key}: {value}")


    # Display the Disk Information section.    

    print("\nDISK INFORMATION")
    print("-----------------------\n") 

    for key, value in disk.items():
        print(f"{key}: {value}")
    
if __name__ == "__main__":
    main()