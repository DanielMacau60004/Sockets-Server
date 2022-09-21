from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverPort = 12000

serverSocket.bind(("", serverPort))

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print("Sent to " + clientAddress[0] + ":" + repr(clientAddress[1]) + " -> " + modifiedMessage)

serverSocket.close()
