import socket

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(("25.28.90.181", 9999))

server.listen(1)

print("waiting for connection")
conn , addr = server.accept()
nick_of_client = input("Enter nickname: ")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"{nick_of_client}: {data}")
    reply = input("You: ")
    conn.send(reply.encode())

conn.close()