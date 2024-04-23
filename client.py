import socket

Server_ip = "localhost"
Server_host = 8002
FORMAT = "utf-8"

CS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CS.connect((Server_ip, Server_host))

file_path = r"D:\hello.txt"

# Open the file in binary mode
with open(file_path, "rb") as file:
    data = file.read()

file_name = "hello.txt"
CS.send(file_name.encode(FORMAT))
msg = CS.recv(1024)
print(msg)

CS.send(data)
msg = CS.recv(1024)
print(msg)

CS.close()
