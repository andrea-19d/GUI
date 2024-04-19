from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
from Crypto.Cipher import AES


def encrypt_aes(raw, key):
    raw = raw.encode('utf-8')
    padded_raw = pad(raw, 16)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded_raw)
    return base64.b64encode(iv + ciphertext)

def decrypt_aes(enc, key):
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    ciphertext = enc[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(ciphertext), 16)
    return decrypted_text.decode('utf-8')
