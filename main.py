import os
import hashlib
from utils.kyber_utils import generate_kyber_keys, key_encapsulation, key_decapsulation
from utils.aes_utils import encrypt_file, decrypt_file
from utils.file_utils import compare_files

def main():
    file_path = input("Enter the file path to encrypt & decrypt: ")

    if not os.path.exists(file_path):
        print("Error: The specified file does not exist.")
        return

    public_key, secret_key = generate_kyber_keys()
    shared_secret, ciphertext = key_encapsulation(public_key)
    recovered_secret = key_decapsulation(secret_key, ciphertext)

    assert shared_secret == recovered_secret, "Key Exchange Failed. Shared secrets do not match."

    aes_key = shared_secret[:32]
    aes_key_hash = hashlib.sha256(aes_key).hexdigest()
    print("AES-256 Encryption Key (SHA-256 Hash):", aes_key_hash, "\n")

    encrypted_file = encrypt_file(file_path, aes_key)
    decrypted_file = decrypt_file(encrypted_file, aes_key)
    compare_files(file_path, decrypted_file)

if __name__ == "__main__":
    main()