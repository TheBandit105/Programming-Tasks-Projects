from collectors.system_info import get_system_info

def main():
    system = get_system_info()
    for key, value in system.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()