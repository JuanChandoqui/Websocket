from time import sleep, time
from client import Client

HOST = "127.0.0.1" #SERVER IP
PORT = 4321 #LISTENING PORT
HEADER = 10
client = Client(HOST, PORT, HEADER)
for i in range ( 10):
    client.sendMessage()
    sleep(10)
client.closeSocket()