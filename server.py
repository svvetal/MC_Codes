import socket

SERVER_IP = "localhost"
SERVER_PORT = 8002
FORMAT = "utf-8"

SS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SS.bind((SERVER_IP, SERVER_PORT))
SS.listen(5)

s1, addr = SS.accept()
file_name = s1.recv(1024).decode(FORMAT)

print("Received file name:", file_name)

# Open the file in binary write mode
with open(file_name, "wb") as file:
    s1.send("File name received".encode(FORMAT))
    print("Receiving file data...")
    while True:
        data = s1.recv(1024)
        if not data:  # If no more data is received, break the loop
            break
        file.write(data)

print("File data received")
s1.send("File data received".encode(FORMAT))

s1.close()
SS.close()
