import base64

from Crypto.PublicKey import RSA
from Backend.AES import decrypt_aes, encrypt_aes
from Backend.DSA import generate_signature, verify_signature
from Backend.RSA_ED import decrypt_rsa, encrypt_rsa
from Crypto.PublicKey import DSA
from Crypto.Random import get_random_bytes


AES_KEY = b'ishdtgrydusbe823'
# AES_KEY = key
print("AES_KEY:" + str(AES_KEY))
RSA_KEY = RSA.generate(2048)
print(f"RSA_KEY: {RSA_KEY}")
DSA_KEY = DSA.generate(1024)


def choose_encryption_algorithm(cipher_type, plaintext):
    if cipher_type == "Symmetric":
        # Perform symmetric decryption (AES)
        ciphertext = encrypt_aes(plaintext, AES_KEY)
        return ciphertext
    elif cipher_type == "Asymmetric":
        # Perform asymmetric decryption (RSA)
        ciphertext = encrypt_rsa(plaintext, RSA_KEY)
        return ciphertext
    elif cipher_type == "DSA":
        ciphertext = generate_signature(plaintext, DSA_KEY)
        return ciphertext

    else:
        return "Invalid cipher type"


def choose_decryption_algorithm(cipher_type, ciphertext, text):
    if cipher_type == "Symmetric":
        # Perform symmetric decryption (AES)
        plaintext = decrypt_aes(ciphertext, AES_KEY)
        return plaintext
    elif cipher_type == "Asymmetric":
        # Perform asymmetric decryption (RSA)
        plaintext = decrypt_rsa(ciphertext, RSA_KEY)
        return plaintext
    elif cipher_type == "DSA":
        result = verify_signature(text, DSA_KEY, ciphertext)
        return result
    else:
        return "Invalid cipher type"
