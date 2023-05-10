

File Hashing and Validation

This Python script demonstrates how to generate a hash for a file and validate it against a known hash value.
Requirements

    Python 3.x

Usage

To generate the hash value for a file, run the script with the path to the file as an argument:

bash

python hashpro.py 
 _    _           _____ _    _            _ _   _     
| |  | |   /\    / ____| |  | |          (_) | | |    
| |__| |  /  \  | (___ | |__| | __      ___| |_| |__  
|  __  | / /\ \  \___ \|  __  | \ \ /\ / / | __| '_ \ 
| |  | |/ ____ \ ____) | |  | |  \ V  V /| | |_| | | |
|_|  |_/_/    \_\_____/|_|  |_|   \_/\_/ |_|\__|_| |_|
                                                      
                                                      
                           _ _                  _ _ 
                          | | |                | | |
 ___  ___  _   _ _ __   __| | |__   __ _ _ __  | | |
/ __|/ _ \| | | | '_ \ / _` | '_ \ / _` | '__| | | |
\__ \ (_) | |_| | | | | (_| | | | | (_| | |    |_|_|
|___/\___/ \__,_|_| |_|\__,_|_| |_|\__,_|_|    (_|_)
                                                    
                                                    

Select an option:
1. SHA256
2. SHA512
3. File Hash
4. File Hash Verify 
5. Quit


To validate the hash value for a file, run the script with the path to the file and the known hash value as arguments:


If the hash value generated for the file matches the known hash value, the script will output "Hashes match." Otherwise, it will output "Hashes do not match."
bash

Select an option:
1. SHA-256
2. SHA-512
3. Exit


2
Enter file path: /home/oneman/Desktop/test.py
Enter expected SHA-512 hash digest: 4b8e80610e0ba75da16dac35eb859354f4445906ff9d654ca039417f2c3b14a9038b7fa44defe34b6f76b5b46d243098d6e4ff50ed7e239a4d7eaf8

Hash verification successful!



Security Considerations

When using hash values for file validation, it's important to use a secure hashing algorithm like SHA-256 to prevent tampering. Additionally, the known hash value should be securely stored and transmitted to prevent interception and modification.
