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

    file_path = input("Enter the file path: ")
    file_hash = hashlib.sha256()

    with open(file_path, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)

    print("The SHA-256 hash of the file is:", file_hash.hexdigest())
def verifyfile():
    import hashlib

    # Prompt user for file path and expected hash digest
    file_path = input("Enter file path: ")
    expected_hash = input("Enter expected SHA-256 hash digest: ")

    # Compute actual hash of file
    BLOCK_SIZE = 65536
    actual_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            actual_hash.update(fb)
            fb = f.read(BLOCK_SIZE)

    # Compare actual hash with expected hash
    if actual_hash.hexdigest() == expected_hash:
        print("Hash verification successful!")
    else:
        print("Hash verification failed. Expected:", expected_hash, "Actual:", actual_hash.hexdigest())


while True:
    print("Select an option:")
    print("1. SHA256")
    print("2. SHA512")
    print("3. FILEHASH")
    print("4. File integrity check ")
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







