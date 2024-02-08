from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    return {
        'ciphertext': b64encode(ciphertext).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8'),
        'nonce': b64encode(cipher.nonce).decode('utf-8')
    }

def decrypt_message(encrypted, key):
    cipher = AES.new(key, AES.MODE_GCM, nonce=b64decode(encrypted['nonce']))
    ciphertext = b64decode(encrypted['ciphertext'])
    tag = b64decode(encrypted['tag'])
    decrypted_message = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted_message.decode('utf-8')

secret_key = get_random_bytes(16)

message_to_encrypt = 'Secret information about you'

encrypted_data = encrypt_message(message_to_encrypt, secret_key)
print("Encrypted Data:", encrypted_data)
decrypted_message = decrypt_message(encrypted_data, secret_key)
print("Decrypted Message:", decrypted_message)
