import json
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

with open('../../../vsomeip_client.json','r') as file:
    data = json.load(file)

data_str = json.dumps(data)
data_bytes = data_str.encode('utf-8')

cipher_text = cipher_suite.encrypt(data_bytes)

with open('encrypted_client.json', 'wb') as file:
    file.write(cipher_text)

