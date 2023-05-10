import hashlib
from pyfiglet import Figlet

custom_fig = Figlet(font='big')
print(custom_fig.renderText('HASH with soundhar !!'))


def SHA256():
    def hash_string(string):
        return hashlib.sha256(string.encode('utf-8')).hexdigest()

    name = input("Enter the message to 256bit hash : ")
    hashed_name = hash_string(name)
    print("The hashed message is:", hashed_name)


def SHA512():
    def hash_string2(string):
        return hashlib.sha512(string.encode('utf-8')).hexdigest()

    name = input("Enter the message to 512bit hash : ")
    hashed_name = hash_string2(name)
    print("The hashed message is:", hashed_name)


def FILEHASH():
    BLOCK_SIZE = 65536

    while True:
        print("Select an option:")
        print("1. SHA-256")
        print("2. SHA-512")
        print("3. Exit")

        choice = input()

        if choice == "1":
            file_path = input("Enter the file path: ")
            file_hash = hashlib.sha256()

            with open(file_path, 'rb') as f:
                fb = f.read(BLOCK_SIZE)
                while len(fb) > 0:
                    file_hash.update(fb)
                    fb = f.read(BLOCK_SIZE)

            print("The SHA-256 hash of the file is:", file_hash.hexdigest())

        elif choice == "2":
            file_path = input("Enter the file path: ")
            file_hash = hashlib.sha512()

            with open(file_path, 'rb') as f:
                fb = f.read(BLOCK_SIZE)
                while len(fb) > 0:
                    file_hash.update(fb)
                    fb = f.read(BLOCK_SIZE)

            print("The SHA-512 hash of the file is:", file_hash.hexdigest())

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
def verifyfile():
    def verify_sha256(file_path, expected_hash):
        BLOCK_SIZE = 65536
        actual_hash = hashlib.sha256()
        with open(file_path, 'rb') as f:
            fb = f.read(BLOCK_SIZE)
            while len(fb) > 0:
                actual_hash.update(fb)
                fb = f.read(BLOCK_SIZE)
        return actual_hash

    def verify_sha512(file_path, expected_hash):
        BLOCK_SIZE = 65536
        actual_hash = hashlib.sha512()
        with open(file_path, 'rb') as f:
            fb = f.read(BLOCK_SIZE)
            while len(fb) > 0:
                actual_hash.update(fb)
                fb = f.read(BLOCK_SIZE)
        return actual_hash

    while True:
        print("Select an option:")
        print("1. SHA-256")
        print("2. SHA-512")
        print("3. Exit")

        choice = input()

        if choice == "1":
            file_path = input("Enter file path: ")
            expected_hash = input("Enter expected SHA-256 hash digest: ")
            actual_hash = verify_sha256(file_path, expected_hash)
            if actual_hash.hexdigest() == expected_hash:
                print("Hash verification successful!")
            else:
                print("Hash verification failed ## ")

        elif choice == "2":
            file_path = input("Enter file path: ")
            expected_hash = input("Enter expected SHA-512 hash digest: ")
            actual_hash = verify_sha512(file_path, expected_hash)
            if actual_hash.hexdigest() == expected_hash:
                print("Hash verification successful!")
            else:
                print("Hash verification failed ## ")

        elif choice == "3":
            break

        else:
            print("Invalid choice")



while True:
    print("Select an option:")
    print("1. SHA256")
    print("2. SHA512")
    print("3. File Hash")
    print("4. File Hash Verify ")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        SHA256()
    elif choice == "2":
        SHA512()
    elif choice == "3":
        FILEHASH()
    elif choice == "4":
        verifyfile()
    elif choice == "5":
        print("___BYE BYE ___ SEE YOU LATER___")
        break
    else:
        print("Invalid choice. Please try again.")
