from socket import *

s = socket(AF_INET, SOCK_STREAM)

host = "127.0.0.1"
port = 7002

s.connect((host,port))

while True:
    text_input = input("Client : ")
    s.send(text_input.encode('utf=8'))
    if text_input == 'Q':
        break;
    received_data = s.recv(2048)
    if received_data.decode('utf=8') == 'Q':
        break;
    print("Server : ",received_data.decode('utf=8'))
s.close()
