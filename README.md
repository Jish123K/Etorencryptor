# Etorencryptor
we're using the PyCryptodome library to perform the encryption and decryption. We're using AES (Advanced Encryption Standard) with CBC (Cipher Block Chaining) mode for encryption and decryption.

For encryption, we're generating a random 32-byte key and a 16-byte initialization vector (IV), and using them to create an AES cipher object. We're then encrypting the file data using the cipher object and writing the IV and encrypted data to a new file with the ".encrypted" extension. We're also printing the encryption key in hexadecimal format.

For decryption, we're asking the user to provide the encryption key in hexadecimal format. We're then reading the IV and encrypted data from the file, and using them along with the encryption key to create an AES cipher object. We're then decrypting the data using the cipher object and writing the decrypted data to a new file with the ".decrypted" extension.
