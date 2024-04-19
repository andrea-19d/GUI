import base64
from Crypto.Cipher import PKCS1_OAEP


def encrypt_rsa(plaintext, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext.encode())
    return base64.b64encode(ciphertext)


def decrypt_rsa(ciphertext, keypair):
    cipher = PKCS1_OAEP.new(keypair)
    plaintext = cipher.decrypt(base64.b64decode(ciphertext)).decode('utf-8')
    return plaintext
