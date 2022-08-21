import socket

lang = input("please enter your Language:")

client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost",5555))

while True:
    message = input("")
    if message == "!q":
        break
    else:
        client.send(f"[{lang}]{message}".encode())