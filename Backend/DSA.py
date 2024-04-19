import base64
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

def generate_signature(plaintext, key):
    h = SHA256.new(plaintext.encode('utf-8'))
    # Create a DSS object with the key
    signer = DSS.new(key, 'fips-186-3')
    # Sign the message and return the digital signature
    signature = signer.sign(h)
    return base64.b64encode(signature)


def verify_signature(plaintext, key, signature):
    h = SHA256.new(plaintext.encode('utf-8'))
    verifier = DSS.new(key, 'fips-186-3')
    try:
        verifier.verify(h, base64.b64decode(signature))
        a = "The signature is authentic."
        return a
    except ValueError:
        b = "The signature is not authentic."
        return b
