from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_file(file_path, key):
    print("Encrypting the File using AES-256")
    cipher = AES.new(key, AES.MODE_CBC)

    with open(file_path, 'rb') as file:
        data = file.read()

    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    enc_file_path = file_path + ".enc"

    with open(enc_file_path, 'wb') as enc_file:
        enc_file.write(cipher.iv)
        enc_file.write(encrypted_data)

    print("File Encrypted Successfully. Encrypted File Path:", enc_file_path, "\n")
    return enc_file_path

def decrypt_file(file_path, key):
    print("Decrypting the Encrypted File")

    with open(file_path, 'rb') as enc_file:
        iv = enc_file.read(16)
        encrypted_data = enc_file.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    decrypted_file_path = file_path.replace(".enc", "_decrypted")
    with open(decrypted_file_path, 'wb') as dec_file:
        dec_file.write(decrypted_data)

    print("File Decryption Completed. Decrypted File Path:", decrypted_file_path, "\n")
    return decrypted_file_path
