from collectors.system_info import get_system_info
from collectors.disk_info import get_disk_info

def main():
    system = get_system_info()
    disk = get_disk_info()

    print("\n======================================================")
    print("FIELDASSIST DEVICE REPORT")
    print("======================================================\n")

    print("\nSYSTEM INFORMATION")
    print("-----------------------\n")

    for key, value in system.items():
        print(f"{key}: {value}")

    print("\nDISK INFORMATION")
    print("-----------------------\n") 

    for key, value in disk.items():
        print(f"{key}: {value}")
    
if __name__ == "__main__":
    main()