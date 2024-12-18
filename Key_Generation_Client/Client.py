import rsa
import socket
import RSA_encrypt_decrypt
import Secret_Phrase_Generator

server_ip = '127.0.0.1'
server_port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((server_ip,server_port))

public_key_bytes_received = sock.recv(4096)

print("This is the public key bytes received from the server:")
print(public_key_bytes_received)

received_public_key = rsa.PublicKey.load_pkcs1(public_key_bytes_received)

with open('public_Key_Server.txt','wb') as p:
    p.write(received_public_key.save_pkcs1('PEM'))

# True random value
seed = input("Enter the Secret Phrase: ")

secret_phrase = str(Secret_Phrase_Generator.generate_int_from_random(seed))

print("This is the secret phrase:")
print(secret_phrase)

encrypted_data = RSA_encrypt_decrypt.encrypt(secret_phrase,received_public_key)

print(encrypted_data)


sock.send(encrypted_data)

sock.close()
