import socket
import RSA_encrypt_decrypt

public_key, private_key = RSA_encrypt_decrypt.loadkeys()

# print(public_key)
# print(private_key)

public_key_bytes = public_key.save_pkcs1(format='PEM')
private_key_bytes = private_key.save_pkcs1(format='PEM')

# print(public_key_bytes)
# print(private_key_bytes)

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1',12348))

client_socket.sendall(public_key_bytes)

encrypted_otp_data = client_socket.recv(1024)

decrypted_otp_data = RSA_encrypt_decrypt.decrypt(encrypted_otp_data,private_key)

print("This is the OTP received from the Server: ")
print(decrypted_otp_data)

with open("My_OTP",'w') as file:
    file.write(decrypted_otp_data)