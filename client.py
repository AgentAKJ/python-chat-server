import socket

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(("25.28.90.181", 9999))
nick_server = input("Nick of server: ")

while True:
    msg = input("You: ")
    client.send(msg.encode())
    response = client.recv(1024).decode()
    print(f"{nick_server}: {response}")