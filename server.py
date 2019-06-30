# Python server
import socket
from Crypto.Cipher import AES

s = socket.socket()
print("Socket successfully created")
# identify port
port = 9500
private_key = 'server private key'
s.bind(('', port))
print("socket binded to %s" %(port)) 

# socket is listening for connection
s.listen(5)
print("socket is listening")
while True:
    (c, addr) = s.accept()
    # show established connection
    print('Got connection from', addr)
    data = c.recv(1024)
    print(data)
    # check if data is hello, return cert to client
    if data == b'Hello':
        cert = 'a certificate'
        c.send(cert)
    else:    
        # reject other data, return goodbye to client
        reject = b"Goodbye"
        c.send(reject)
    # get public key from client
    sp_key = c.recv(1024)
    message = 'unlock'
    private_key2 = AES.new('private key', AES.MODE_CBC, sp_key)
   

    c.send(private_key2.decrypt(message))
    
    c.close()