import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1025))
message = s.recv(1024)
# This 1024 is for byte and not the port number
print(message.decode("utf-8"))