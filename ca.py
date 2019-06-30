# certificate authority
        
def validateCert(cert):
    registered_cert = 'a certificate'
    public_key = 'public key for server'
    
    if cert == registered_cert:
        return public_key
    else:
        return 'Null'    


