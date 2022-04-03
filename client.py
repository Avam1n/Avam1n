import socket

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
s_port = 8000

print("=" * 66)
print("Соединение произошло успешно!")
print(f"Это твой IP: {ip}")
print("=" * 66)

server_host = input("Введите IP дурга: ")
name = input("Введите имя:")

socket_server.connect((server_host, s_port))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(f"{server_name}, вошёл в чат...")

while True:
    messsage = (socket_server.recv(1024).decode())
    print(f"{server_name}: {messsage}")
    messsage = input("Я: ")
    socket_server.send(messsage.encode())

    if messsage.upper() == '\q':
        socket.close()
        print(f'{name} вышел из чата!!!')
