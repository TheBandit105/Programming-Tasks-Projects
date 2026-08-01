from collectors.system_info import get_system_info
from collectors.disk_info import get_disk_info

def main():
    system = get_system_info()
    disk = get_disk_info()

    for key, value in system.items():
        print(f"{key}: {value}")

    print(disk)


    
if __name__ == "__main__":
    main()