from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_rsa(text, public_key):
    cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    return base64.b64encode(cipher.encrypt(text.encode())).decode()

def decrypt_rsa(encrypted_data, private_key):
    cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
    return cipher.decrypt(base64.b64decode(encrypted_data)).decode()

# مثال استفاده
private_key, public_key = generate_rsa_keys()
encrypted = encrypt_rsa("متن محرمانه", public_key)
print(decrypt_rsa(encrypted, private_key))