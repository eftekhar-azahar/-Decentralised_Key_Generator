import socket
import rsa
import RSA_encrypt_decrypt
import random

all_keys = []

with open('key_store.txt','r') as file:
    for line in file:
        cleaned_line = line.strip()
        all_keys.append(cleaned_line)

# print(all_keys)

def choose_key():
    size = len(all_keys)
    start = 0
    index = random.randint(start,size-1)
    return all_keys[index]

# print(choose_key())


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1',12348))

server_socket.listen(5)

while True:
    print('Waiting for the connection from the OTP requesting Client:')
    connection, client_address = server_socket.accept()
    print("Connected to : ", client_address)

    public_keys_bytes_received = connection.recv(1024)

    print(public_keys_bytes_received)

    received_public_key = rsa.PublicKey.load_pkcs1(public_keys_bytes_received)

    print(received_public_key)

    OTP = choose_key()

    encrypted_otp_data = RSA_encrypt_decrypt.encrypt(OTP,received_public_key)

    print('This is the encrypted OTP data: ')
    print(encrypted_otp_data)

    connection.send(encrypted_otp_data)


