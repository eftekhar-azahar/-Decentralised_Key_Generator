import socket
import rsa
import Generate_Server_Keys
import RSA_encrypt_decrypt
import Generate_Server_Keys
import Response_Phrase_Generator

public_key,private_key = RSA_encrypt_decrypt.loadkeys()

print(public_key)
print(private_key)

public_key_bytes = public_key.save_pkcs1(format='PEM')
print("------------------------------------------------------------------")
print(public_key_bytes)
private_key_bytes = private_key.save_pkcs1(format='PEM')

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',12345))
server_socket.listen(5)

while True:
    print("Waiting for the connection .......")
    connection,client_address = server_socket.accept()
    print(f"Connected to {client_address}")
    print("Connection Made Successfully!")

    connection.sendall(public_key_bytes)

    received_encrypted_data = connection.recv(4096)

    print("This is the encrypted secret value: ")
    print(received_encrypted_data)

    decrypted_secret_value = RSA_encrypt_decrypt.decrypt(received_encrypted_data,private_key)

    print("This is the decrypted value from the key generating client: ")
    print(decrypted_secret_value)

    response_secret_phrase = Response_Phrase_Generator.generate_int_from_random(int(decrypted_secret_value))

    with open("key_store.txt",'a') as file:
        file.write(str(response_secret_phrase) + "\n")

    connection.close()







