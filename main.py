from Crypto.Cipher import AES

from Crypto.Random import get_random_bytes

import hashlib

def encrypt_file():

    location = input("Please provide the file location to encrypt: ")

    key = get_random_bytes(32)

    iv = get_random_bytes(16)

    try:

        with open(location, 'rb') as file:

            original = file.read()

        cipher = AES.new(key, AES.MODE_CBC, iv)

        encrypted = cipher.encrypt(original)

        with open(location + ".encrypted", 'wb') as encrypted_file:

            encrypted_file.write(iv + encrypted)

        print("File encrypted successfully")

        print("=============================================")

        print("Encryption key:", key.hex())

    except:

        print("Failed to encrypt the file")

def decrypt_file():

    location = input("Please provide the file location to decrypt: ")

    key_hex = input("Please provide the encryption key in hex format: ")

    try:

        with open(location, 'rb') as enc_file:

            iv = enc_file.read(16)

            encrypted = enc_file.read()

        key = bytes.fromhex(key_hex)

        cipher = AES.new(key, AES.MODE_CBC, iv)

        decrypted = cipher.decrypt(encrypted)

        with open(location.replace(".encrypted", ""), 'wb') as dec_file:

            dec_file.write(decrypted)

        print("File decrypted successfully")

        print("=============================================")

    except:

        print("Failed to decrypt the file")

def menu():

    print("0 - Exit")

    print("1 - Encrypt File")

    print("2 - Decrypt File")

    user_option = input("Your option: ")

    if user_option == "0":

        return

    elif user_option == "1":

        encrypt_file()

    elif user_option == "2":

        decrypt_file()

    else:

        print("Invalid option provided")

    menu()

def initialize():

    print("Please provide your option:\n")

    print("1 - Encrypt/Decrypt File")

    user_option_input = input("Your option: ")

    if user_option_input == "1":

        menu()

    else:

        print("invalid option provided")

initialize()

