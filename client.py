import socket

s = socket.socket()
s.connect(('localhost', 8000))

server_time = s.recv(1024).decode()
print("Received from server:", server_time)

s.send("Acknowledgment received from client.".encode())

s.close()