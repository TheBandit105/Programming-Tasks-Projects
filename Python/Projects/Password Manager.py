from cryptography.fernet import Fernet
import os

# Function to generate and save a key (run once to generate 'key.key')
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

# Function to load the key from the file
def load_key():
    if not os.path.exists('key.key'):
        print("Key file not found! Generating a new key...")
        write_key()
    
    with open('key.key', 'rb') as file:
        key = file.read()
    return key

# Load the encryption key
key = load_key()
fer = Fernet(key)

def view():
    if not os.path.exists('passwords.txt'):
        print("No stored passwords found.")
        return

    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            if '|' in data:
                user, encrypted_passw = data.split('|')
                try:
                    decrypted_passw = fer.decrypt(encrypted_passw.encode()).decode()
                    print(f'User: {user} | Password: {decrypted_passw}')
                except Exception as e:
                    print(f'Error decrypting password for {user}: {e}')


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()

    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + encrypted_pwd + '\n')

while True:
    mod = input("Would you like to add a new password or view existing ones (view, add)? Press q to quit. ").lower()

    if mod == 'q':
        break
    elif mod == 'view' or mod == 'V' or mod == 'v':
        view()
    elif mod == 'add' or mod == 'A' or mod == 'a':
        add()
    else:
        print('Invalid mode.')
