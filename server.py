import socket
from datetime import datetime

# Create a socket object
s = socket.socket()
# Bind to localhost on port 8000
s.bind(('localhost', 8000))
# Listen for a connection
s.listen(5)

# Accept a connection
c, addr = s.accept()
print("Client Address :", addr)

# Get current time
now = datetime.now()
# Send the formatted date/time to the client
c.send(now.strftime("%d/%m/%Y %H:%M:%S").encode())

# Receive acknowledgment from the client
ack = c.recv(1024).decode()
if ack:
    print(ack)

# Close the connection
c.close()
