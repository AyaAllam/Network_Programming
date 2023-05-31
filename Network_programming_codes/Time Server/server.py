import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostbyname(), 1024))
s.bind((socket.gethostname(), 1025))
# 1024 is the port no. The port no can be >= 1024 because the rest are reserved
s.listen(5)
#from datetime import date
import datetime

dateAsString = str(datetime.datetime.now())

x=dateAsString.encode()
while True:
    clt, adr = s.accept()
    print(f"Connection to {adr} is established")
    clt.send(x)
# Since bytes is used utf-8 tells what kind of byte is used