import rsa

def generate_client_keys():
    public_key, private_key = rsa.newkeys(2048)
    print(public_key)
    print(private_key)

    with open('public_Key_Client.pem','wb') as p:
        p.write(public_key.save_pkcs1('PEM'))

    with open('private_Key_Client.pem','wb') as p:
        p.write(private_key.save_pkcs1('PEM'))


generate_client_keys()