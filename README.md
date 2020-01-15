# Python Encryption
## Assignment for class: Encrypting with Python

### The goals of the assignment are:

1) The client will initiate contact with the server.

2) The server will respond to the client with its certificate.

3) The client will validate the certificate and potentially get a public key.  If a public key is provided by the CA, the client will use the public key to encryp a 'session cipher key' and send to the server.

4) The server will either receive a goodbye (because it wasn't recognized) or a 'session cipher key' encrypted with its public key.  The server will decrypt the 'session cipher key' using its private key.   The server will respond to the client some kind of acknowledgement using the 'session cipher key'.

5) The client will receive the acknowledgement, decrypt to validate and begin transferring data.

6) You are to have the client and server exchange some data at this point and include necessary methods to show the data has been encrypted and decrypted successfully.

