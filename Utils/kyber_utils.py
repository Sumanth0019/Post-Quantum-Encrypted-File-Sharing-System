from kyber_py.kyber import Kyber512

def generate_kyber_keys():
    print("\nGenerating Kyber-512 Key Pair")
    public_key, secret_key = Kyber512.keygen()
    print("Public Key Generated:", public_key.hex()[:64], "...")
    print("Secret Key Generated:", secret_key.hex()[:64], "...\n")
    return public_key, secret_key

def key_encapsulation(public_key):
    print("Performing Key Encapsulation")
    shared_secret, ciphertext = Kyber512.encaps(public_key)
    print("Shared Secret Encapsulated:", shared_secret.hex()[:64], "...")
    print("Ciphertext (Encrypted Key):", ciphertext.hex()[:64], "...\n")
    return shared_secret, ciphertext

def key_decapsulation(secret_key, ciphertext):
    print("Decapsulating the Shared Secret")
    recovered_secret = Kyber512.decaps(secret_key, ciphertext)
    print("Recovered Shared Secret:", recovered_secret.hex()[:64], "...\n")
    return recovered_secret
