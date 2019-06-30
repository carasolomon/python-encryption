# Python client
import socket
from Crypto.Cipher import AES
import ca

s = socket.socket()

port = 9500
# connect to server
s.connect(('127.0.0.1', port))

# send message to server
message = b"Hello"
s.send(message)

# get certificate
get_cert = s.recv(1024)
message = 'a message'
# validate certificate from Certificate Authority
public_key = ca.validateCert(get_cert)
private_key = AES.new('private key', AES.MODE_CBC, public_key)

if public_key != 'null':
    ciphertext = private_key.encrypt(message)
    s.send(ciphertext)
else:
    s.send(b'Goodbye')    



print(s.recv(1024))
s.close()
